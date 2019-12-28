import cv2

img=cv2.imread("ravi.jpg")
print(img)
print(type(img))
print(img.shape)
cv2.imshow("legend",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
resized_image=cv2.resize(img,(650,600))

cv2.imshow("legend",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
resized_image=cv2.resize(img,(int(img.shape[1])/3),(int((img.shape[0])/3)))
cv2.imshow("legends",resized_image)
