import cv2

def resize_image(image, width = 600, height = 400):
    '''RESIZING IMAGES'''
    #resize image window
    resized_image = cv2.resize(image, (width, height))
    return resized_image


def convert_to_grayscale(resized_image):
    resized_gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    return resized_gray_image

def show_grayscale(resized_gray_image):  
    #displays the grayscale image
    cv2.imshow("Grayscale Image", resized_gray_image)
    
def show_edges(resized_gray_image):
    '''EDGE DETECTION'''
    #detecting edges in the image using Canny edge detection
    edges = cv2.Canny(resized_gray_image,200, 100)
    #displays the edges detected in the image
    cv2.imshow("Edges Detected", edges)



def binary_thresholding(resized_gray_image):
    ''' BINARY THRESHOLDING'''
    #binary thresholding
    _, binary_image = cv2.threshold(resized_gray_image, 120, 255, cv2.THRESH_BINARY)
    #displays the binary image
    cv2.imshow("Binary Image", binary_image)
    
def detect_contours(resized_image):
    '''CONTOUR DETECTION'''
    #finding edges
    edges = cv2.Canny(resized_image, 200, 200)
    #finding contours
    contours, _ =cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #drawing contours 
    contours_image = resized_image.copy()
    cv2.drawContours (contours_image, contours, -1, (0,255,0), 2)
    #displays the contours on image
    cv2.imshow("Contours Detected", contours_image)
    

#Reads the image 
image = cv2.imread(r"images/sample image.jpg")
resized_image = resize_image(image)
resized_gray_image = convert_to_grayscale(resized_image)


if image is None:
    print("Error: Could not read the image.")
else:
    choice =input("What would you like to do with the image?\n" \
    "1. Convert to Grayscale\n" \
    "2. Show edges\n" \
    "3. Perform Binary Thresholding\n" \
    "4. Detect Contours\n" \
    "Enter the number corresponding to your choice: ")

    if choice == '1':
        show_grayscale(resized_gray_image)
    elif choice == '2':
        show_edges(resized_gray_image)
    elif choice == '3':
        binary_thresholding(resized_gray_image)
    elif choice == '4':
        detect_contours(resized_image)
    else:
        print("Invalid choice. Please select a valid option.")

#displays the image
#cv2.imshow("Image", image)

'''DISPLAYING RESIZED IMAGES
cv2.imshow("Resized Image", resized_image)
cv2.imshow("Resized Grayscale Image", resized_gray_image)
'''

#Waits for a key press to close the displayed image
cv2.waitKey(0)
cv2.destroyAllWindows()