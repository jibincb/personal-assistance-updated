import cv2
import numpy as np
import concurrent.futures
import time
from collections import Counter

def most_frequent(arr):
    counter = Counter(arr)
    most_common = counter.most_common(1)
    return most_common[0][0]
def is_dark(image, threshold=100):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate the average pixel value (intensity)
    intensity = np.mean(gray)

    # Make a binary decision based on the threshold
    return intensity < threshold
avg_light = []
def check_light_condition():
    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    # while True:
    #     # Capture a frame
    #     ret, frame = cap.read()
    #
    #     # Check if the room is dark
    #     dark_condition = is_dark(frame)
    #
    #     # Display the frame and the result
    #     cv2.imshow('Frame', frame)
    #     print(f'Room is {"Dark" if dark_condition else "Bright"}')
    #
    #     # Break the loop if 'q' key is pressed
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
        # Capture a frame
    ret, frame = cap.read()

        # Check if the room is dark
    dark_condition = is_dark(frame)

        # Display the frame and the result

    cv2.imshow('Frame', frame)
    print(f'Room is {"Dark" if dark_condition else "Bright"}')
    return dark_condition


        # Break the loop if 'q' key is pressed

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    check_light_condition()
