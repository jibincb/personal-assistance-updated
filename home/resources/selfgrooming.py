from PIL import Image
from transformers import pipeline
import cv2

vqa_pipeline = pipeline("visual-question-answering")


def self_grooming():
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()


    ret, frame = cap.read()


    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))


    questions = ['What dress is that?',"What is the design of dress?",'what is the colour of dress?', 'what is meterial did the dress made of?','what is the best occasion the cloth can be worn?', 'Whether this dress is worn by men or women or both men and women?', "Is it half sleeve or full sleeve."]
    prompt = 'is there any clothes?'
    a = vqa_pipeline(image, prompt, top_k = 1)
    print(a)
    c = a[0]['answer']
    # List to store answers
    details = []


    if c == 'yes':
        for question in questions:
            answer = vqa_pipeline(image, question, top_k=1)
            details.append(answer[0]['answer'])


        cap.release()
        return (
            f"The dress is {details[0]}. It has a {details[1]} design. Its colour is {details[2]}. It seems to be made of {details[3]}. It can be worn in occasions like {details[4]}.  It is worn by {details[5]}. It is {details[6]} sleeve.")
    else:
        return "No clothes found"
# print(self_grooming())
