import cv2

video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

#GRAYSCALE CONVERSION
def gray_scale(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale Webcam", gray_frame)

#EDGE DETECTION
def get_edges(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_frame, 200, 100)
    cv2.imshow("Edges Detected Webcam", edges)

#BINARY THRESHOLDING
def binary_threshold(frame):
    _, binary_frame = cv2.threshold(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary Image Webcam", binary_frame)

#CONTOUR DETECTION
def detect_contours(frame):
    edges = cv2.Canny(frame, 100, 200)
    contours, _ =cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_frame = frame.copy()
    cv2.drawContours (contours_frame, contours, -1, (0,255,0), 2)
    cv2.imshow("Contours Detected Webcam", contours_frame)

#ORIGINAL IMAGE 
def original_frame(frame):
    cv2.imshow("Original Webcam Feed", frame)

choice =input("What would you like to do with the webcam feed?\n" \
    "0. Show original feed\n" \
    "1. Convert to Grayscale\n" \
    "2. Show edges\n" \
    "3. Perform Binary Thresholding\n" \
    "4. Detect Contours\n" \
    "Enter choice (0-4): ")

while(True):
    rect,frame = video_capture.read()

    if choice == "0":
        original_frame(frame)
    elif choice == "1":
        gray_scale(frame)
    elif choice == "2":
        get_edges(frame)
    elif choice == "3":
        binary_threshold(frame)
    elif choice == "4":
        detect_contours(frame)
    

    #error handling
    if not rect:
     print("Error, can't find camera.")
     break
    
     #exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
      break
video_capture.release()
cv2.destroyAllWindows()