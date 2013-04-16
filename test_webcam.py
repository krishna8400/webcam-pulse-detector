import cv2, numpy

#Create object to read images from camera 0
cam = cv2.VideoCapture(0)

while True:
    #Get image from webcam
    ret, img = cam.read()
    
    #create some test points
    pts1 = numpy.array([[0,0],[100,100]])
    pts2 = numpy.array([[0,0],[0,500],[200,200]],numpy.int0)
    
    #test out the polylines function
    cv2.polylines(img, [pts1, pts2], False, (255,255,255),1)
    
    #show the result
    cv2.imshow("Camera", img)

    #Sleep infinite loop for ~10ms
    #Exit if user presses <Esc>
    if cv2.waitKey(10) == 27:
        break
