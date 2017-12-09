import cv2
import os

# image = cv2.imread('./images/ham1.jpg')
# std_image = cv2.resize(image, (60,60))
test = cv2.resize(cv2.imread('./test.jpg'),(60,40))

print(os.listdir('./images'))
dataset = os.listdir('./images')
dis = []
for data in dataset:
    image = cv2.resize(cv2.imread(('./images/'+data)),(60,40))
    # val = image - test
    val = 0
    for i in range(60):
        for j in range(40):
            for k in range(3):
                val += (image[i][j][k]-test[i][j][k])**2
    dis.append(val)
#
print(dis)
# print(dis.index(max(dis)))
# while True:
#     cv2.imshow('d',test)
#     if cv2.waitKey(0):
#         break
# print(image)
