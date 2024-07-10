import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    ## Basic shapes ##

    ## two line making an X on the feed ##

    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
    img = cv2.line(img, (0,height), (width,0), (0,255,0), 5)

    ## rectangle draw on feed ##
    img = cv2.rectangle(img, (100,100), (200,200), (128, 128, 128), 5)

    ## circle draw on feed ##
    img = cv2.circle(img, (300, 300), 75, (0,0,255), 15)

    ## drawing text on feed ##

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'I am GREAT!', (10, height - 10), font, 2, (0,0,0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
