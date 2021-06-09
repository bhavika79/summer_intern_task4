import cv2

nature1=cv2.imread("nature1.jpg")

cv2.imshow("image1",nature1)
cv2.waitKey()
cv2.destroyAllWindows()

nature2=cv2.imread("nature2.jpg")

cv2.imshow("image2",nature2)
cv2.waitKey()
cv2.destroyAllWindows()

fimage=cv2.hconcat([nature1,nature2])

cv2.imshow("merged_image",fimage)
cv2.waitKey()
cv2.destroyAllWindows()