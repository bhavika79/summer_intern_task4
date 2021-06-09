import cv2
photo1=cv2.imread("dog.jpg")
photo2=cv2.imread("cat1.jpg")

cv2.imshow("dog",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("cat",photo2)
cv2.waitKey()
cv2.destroyAllWindows()

photo1.shape
photo2.shape

temp1=photo1[10:190,95:265].copy()
temp2=photo2[50:230,205:375].copy()

photo1[10:190,95:265]=temp2
photo2[50:230,205:375]=temp1

cv2.imshow("swap1",photo1)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("swap2",photo2)
cv2.waitKey()
cv2.destroyAllWindows()