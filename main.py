import cv2


def resize_img(img):
    scale_percent = 20
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


image = cv2.imread("C:\\Users\\Cosmin\\Desktop\\Export\\Cosmin_DSC_01.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
color = cv2.bilateralFilter(image, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

# cv2.imshow("Image", image)
# cv2.imshow("edges", edges)
cartoon = resize_img(cartoon)
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
