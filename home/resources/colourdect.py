import cv2
import numpy as np

def detect_dominant_color(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges for red, green, and blue
    color_ranges = {
        'Red': ((0, 100, 100), (10, 255, 255)),
        'Green': ((40, 40, 40), (80, 255, 255)),
        'Blue': ((100, 100, 100), (140, 255, 255)),
    }

    detected_colors = []

    for color_name, (lower, upper) in color_ranges.items():
        # Threshold the image to get a binary mask for the color
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

        # Check if there are non-zero pixels in the mask
        if cv2.countNonZero(mask) > 0:
            detected_colors.append(color_name)

    # Return the dominant color (first color in the list)
    return detected_colors[0] if detected_colors else None

def main():
    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame
        ret, frame = cap.read()

        # Detect and print the dominant color
        dominant_color = detect_dominant_color(frame)
        if dominant_color:
            print(f'Dominant Color: {dominant_color}')
            return dominant_color
        # Display the original frame
        cv2.imshow('Original Frame', frame)

        # Check if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
