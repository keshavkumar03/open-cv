import cv2

# Create a VideoCapture object to access the default camera
cap = cv2.VideoCapture(0)
cap.set(10,6400)


# Check if the camera is opened successfully
if not cap.isOpened():
    print("Unable to open the camera")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Unable to read frame from camera")
        break

    # Display the frame using cv2.imshow
    cv2.imshow("Webcam", frame)

    # Wait for 1 millisecond for a key event (pressing any key) and break the loop if the key is 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
