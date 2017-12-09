import cv2

image = cv2.imread('test.jpg')
while True:
    cv2.imshow('tmp',image)
    if cv2.waitKey(0):
        break
# print(image)
