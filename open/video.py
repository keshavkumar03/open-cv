import cv2

# Create a VideoCapture object to read the video file
cap = cv2.VideoCapture('resource/vathi.mp4')

# Check if the video file is opened successfully
if not cap.isOpened():
    print("Unable to open the video file")
    exit()

while True:
    # Read a frame from the video file
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Unable to read frame from video file")
        break

    # Display the frame using cv2.imshow
    cv2.imshow("Video", frame)

    # Wait for 25 milliseconds for a key event (pressing any key) and break the loop if the key is 'q'
    if cv2.waitKey(25) == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
