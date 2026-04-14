import cv2
import os

cap = cv2.VideoCapture(1)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display the frame
    cv2.imshow('Live View', frame)

    # Wait for key press
    key = cv2.waitKey(1)
    if key == ord('1'):
        cv2.imwrite('current_files/front_temp.png', frame)
        os.replace('current_files/front_temp.png', 'current_files/front.png')
        print("Front photo stored")
    if key == ord('2'):
        cv2.imwrite('current_files/rear_temp.png', frame)
        os.replace('current_files/rear_temp.png', 'current_files/rear.png')
        print("Rear photo stored")

    elif key == ord('q'):  # Press 'q' to quit
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()