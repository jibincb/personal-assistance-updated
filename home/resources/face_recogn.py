import cv2
from deepface import DeepFace
from collections import Counter
import time
import os


def most_frequent(avg_face):
    most_common = Counter(avg_face).most_common(1)
    if most_common:
        return most_common[0][0]
    else:
        return None



avg_face = []

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def FindFace(frame):
    try:
        # Save the frame as an image file
        # img_path = 'temp_frame.jpg'
        # cv2.imwrite(img_path, frame)

        # Perform face recognition on the saved image
        df = DeepFace.find(img_path=frame, db_path='home/resources/faces', model_name='VGG-Face', distance_metric='cosine')
        print(df)

        if len(df) != 0:

            if not df[0]['identity'].empty:
                name = df[0]['identity'][0]
                image_name = os.path.basename(name).replace('.jpg', '')
                print(image_name)
                return image_name
        else:
            print("No face found in the database")
            return "Error"
    except ValueError:
        print("Face not found in the database")
        print(ValueError)
        return "Error"


def process_frame(frame):
    face = FindFace(frame)
    cv2.putText(frame, face, (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
    if face != None:
        avg_face.append(face)
    time.sleep(1)
    cv2.imshow("video", frame)


def face_regn():
    c = 0
    while c < 10:
        ret, frame = cap.read()

        if ret:
            process_frame(frame)

        c += 1

    result = most_frequent(avg_face)
    cap.release()
    cv2.destroyAllWindows()

    if result == None:
        return("None")
    else:
        return(result)


# face_regn()
