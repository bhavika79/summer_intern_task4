import cv2
import numpy as np

image=np.zeros((500,500,3))
cv2.imshow("i1",image)
cv2.waitKey()
cv2.destroyAllWindows()

image[0:500,0:500]=(255,255,255)
cv2.imshow("i1",image)
cv2.waitKey()
cv2.destroyAllWindows()

image=cv2.rectangle(image,(100,200),(350,325),(0,0,0),3)
image=cv2.line(image,(100,200),(135,100),(0,0,0),3)
image=cv2.line(image,(170,200),(135,100),(0,0,0),3)
image=cv2.line(image,(170,200),(170,325),(0,0,0),3)
image=cv2.line(image,(135,100),(350,100),(0,0,0),3)
image=cv2.line(image,(350,200),(350,100),(0,0,0),3)

cv2.imshow("final_image",image)
cv2.waitKey()
cv2.destroyAllWindows()