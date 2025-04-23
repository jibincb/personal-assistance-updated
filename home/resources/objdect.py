import torch
import cv2
import time
import pyttsx3



model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)


cap = cv2.VideoCapture(0)
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def dectobj(text):
    c = 0
    while c < 10:
        ret, frame = cap.read()  # Read a frame from the camera

        if not ret:
            print("Error: failed to capture frame")
            break

        # Convert frame from BGR to RGB (YOLOv5 expects RGB input)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run YOLOv5 on the frame
        results = model(rgb_frame)

        detected_objects = results.pandas().xyxy[0]['name']
        print(detected_objects)
        time.sleep(1)

        for ele in detected_objects:
            if ele == text:
                print(f'{text} found!')
                speak(f'{text} found!')
                break
        else:
            print(f'{text} not found.')
            speak(f'{text} not found!')


        cv2.imshow('Frame', frame)
        c += 1


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

