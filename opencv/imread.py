import cv2
import os
WIDTH = 920
HEIGHT = 80
# image = cv2.imread('./images/ham1.jpg')
# std_image = cv2.resize(image, (60,60))
test = cv2.resize(cv2.imread('./test.jpg'),(WIDTH,HEIGHT))

print(os.listdir('./images'))
dataset = os.listdir('./images')
dis = []
width = 24
height = 16
for data in dataset:
    image = cv2.resize(cv2.imread(('./images/'+data)),(WIDTH,HEIGHT))
    # val = image - test
    val = {"dis": 0, "type": data}
    for i in range(HEIGHT/height):
        for j in range(WIDTH/width):
            pix = 0
            for y in range(height):
                for x in range(width):
                    for k in range(3):
                        pix += image[i*height+y][j*width+x][k]
            val["dis"] += pix**2
            # for k in range(3):
            #     val["dis"] += abs(image[i][j][k]-test[i][j][k])
    dis.append(val)
#
# print(sorted(dis))
dis.sort()
# for item in dis:
#     print(item)
# print(dis.index(max(dis)))
while True:
    cv2.imshow('d',test)
    if cv2.waitKey(0):
        break
# print(image)
