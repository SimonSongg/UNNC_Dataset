import cv2
import numpy as np
import os

#########

# dir
targetDir = r"E:\ADV\UNNC_Dataset\20210822"

#########

dirListRGB8 = os.listdir(targetDir + r"\rgb8")
dirListZ16 = os.listdir(targetDir + r"\z16")

index = int(os.path.splitext(dirListRGB8[0])[0])

for tempDir in dirListRGB8:
    if index > int(os.path.splitext(tempDir)[0]):
        index = int(os.path.splitext(tempDir)[0])
for tempDir in dirListZ16:
    if index > int(os.path.splitext(tempDir)[0]):
        index = int(os.path.splitext(tempDir)[0])

matRGB8 = cv2.imread(targetDir + r"\rgb8" + "\\" + str(index) + ".png")
matZ16 = cv2.imread(targetDir + r"\z16" + "\\" + str(index) + ".png")

if matRGB8 is None:
    cv2.imshow("RGB8", nullImg)
else:
    cv2.putText(matRGB8, str(index), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("RGB8", matRGB8)

if matZ16 is None:
    cv2.imshow("Z16", nullImg)
else:
    cv2.putText(matZ16, str(index), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Z16", matZ16)

while True:
    key = cv2.waitKey(0)

    if key == 97:       #a
        #if index != 0:
        index = index - 1
    elif key == 100:    #d
        index = index + 1
    elif key == 120:    #x
        if os.path.exists(targetDir + r"\rgb8" + "\\" + str(index) + ".png"):
            os.remove(targetDir + r"\rgb8" + "\\" + str(index) + ".png")
        if os.path.exists(targetDir + r"\z16" + "\\" + str(index) + ".png"):
            os.remove(targetDir + r"\z16" + "\\" + str(index) + ".png")
        index = index + 1
    elif key == 107:    # k
        break

    matRGB8 = cv2.imread(targetDir + r"\rgb8" + "\\" + str(index) + ".png")
    matZ16 = cv2.imread(targetDir + r"\z16" + "\\" + str(index) + ".png")

    if matRGB8 is None:
        nullImg = np.zeros((720, 1280, 3), np.uint8)
        cv2.putText(nullImg, str(index), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("RGB8", nullImg)
    else:
        cv2.putText(matRGB8, str(index), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("RGB8", matRGB8)

    if matZ16 is None:
        nullImg = np.zeros((720, 1280, 3), np.uint8)
        cv2.putText(nullImg, str(index), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Z16", nullImg)
    else:
        cv2.putText(matZ16, str(index), (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow("Z16", matZ16)
