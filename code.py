import cv2
cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
while(True):
    f,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=cascade.detectMultiScale(gray,1.1,3)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
    cv2.imshow('img',img)
    k=cv2.waitKey(29) & 0xff
    if(k==27):
        break
cam.release()
