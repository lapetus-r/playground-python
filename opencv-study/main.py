import cv2

# 이미지 파일 로드
image = cv2.imread("files/yumtory.png")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.circle(gray_image, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)
cv2.circle(gray_image, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)

# 결과 이미지 출력
cv2.imshow("Original Image", image)
cv2.waitKey(0)

cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
