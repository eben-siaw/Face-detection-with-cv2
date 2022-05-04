# import cv2 

# cam = cv2.VideoCapture  
import cv2 as cv


cam = cv.VideoCapture(0) 
cam.set(3, 600)
cam.set(4, 500) 

faceDetector = cv.CascadeClassifier('haarcascade_frontface_default.xml')

while True: 
    retv, frame = cam.read() 
    warna = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(warna, 1.3, 5)
      
    for(x, y, w, h) in faces: 
        frame = cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 63), 2)
        rec_maka = warna[y: y + h, x: x +w]
           
    cv.imshow('Webcam', frame)
    close = cv.waitKey(1) & 0xFF
    if close == 27 or close == ord('n'): 
       break

cam.release()
cv.destroyAllWindows()

# print("Hello this is from today")

