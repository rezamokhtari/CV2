import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.line(frame,(100,200),(300,400),(0,0,255),10)
    #cv2.rectangle(frame, (100,200),(200,300),(0,255,0),10)
    pts = np.array([[10,12],[15,17],[22,76],[50,20]])

    cv2.circle(frame,(200,200),70,(255,0,0),5)
    cv2.polylines(frame,[pts],True,(0,255,0),5)

    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(frame,'Hello World',(100,100),font,1,(250,0,140),5)

    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()