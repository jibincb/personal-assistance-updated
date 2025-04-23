import cv2
import os
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch


model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}


def predict_caption_from_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        return

    cv2.imshow("Camera", frame)
    cv2.waitKey(1000)

    cv2.imwrite("captured_image.jpg", frame)
    cap.release()
    cv2.destroyAllWindows()

    image_path = "captured_image.jpg"
    caption = predict_caption([image_path])
    print("Caption:", caption)

    os.remove(image_path)
    return caption[0]

def predict_caption(image_paths):
    images = []
    for path in image_paths:
        try:
            image = cv2.imread(path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            images.append(image)
        except Exception as e:
            print(f"Error loading image {path}: {e}")

    inputs = feature_extractor(images=images, return_tensors="pt")
    pixel_values = inputs.pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    print("Final Caption Is:", preds)
    return preds

