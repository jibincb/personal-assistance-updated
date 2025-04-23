from PIL import Image
from transformers import pipeline
import cv2

# Initialize the VQA pipeline
vqa_pipeline = pipeline("visual-question-answering")

# Open a video capture device (0 for the default camera)
def occasion(text):
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the OpenCV frame to a PIL image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # List of questions
    question = text
    prompt = 'is there any clothes?'
    a = vqa_pipeline(image, prompt, top_k = 1)
    print(a)
    c = a[0]['answer']



    if c == 'yes':
        answer = vqa_pipeline(image, question, top_k=1)
        answer = answer[0]['answer']


        cap.release()
        if answer == 'yes':
            return f"Yes. It can be worn in this occasion"
        else:
            return f"No. It cannot be worn in this occasion"
    else:
        return "No clothes found"
# print(occasion('is this dress is good for funeral?'))