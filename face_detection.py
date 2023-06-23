#!/usr/bin/env python
# coding: utf-8

# In[15]:


import cv2

#importing the face recogonisation algorithm
alg="haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)

#captures the video
cam=cv2.VideoCapture(0)

#loop to detect the face ineach frame
while True:
    
    #reads the camera frame and changes into a gray image
    _,img=cam.read()
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    text = "No"
    
    #detects the multiscale i.e eyes, nose, mouth and face
    face=haar_cascade.detectMultiScale(gray_img,1.3,4)
    
    #draw the rectange on the face
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
        text="Face detected"
    
    #displays the output
    cv2.putText(img,text,(10,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),4)
    cv2.imshow("faceDetection",img)
    
    #if esca button is pressed the camera is closed
    key=cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()


# In[ ]:




