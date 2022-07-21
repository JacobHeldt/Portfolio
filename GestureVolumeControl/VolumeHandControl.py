import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
import osascript


#################################
wCam, hCam = 640, 480
#################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.75)


minVol = 0
maxVol = 100


################################################################
# result = osascript.osascript('get volume settings')
# print(result)
# print(type(result))
# volInfo = result[1].split(',')
# outputVol = volInfo[0].replace('output volume:', '')
# print(outputVol)
###############################################################


###############################################################
# target_volume = 100
# vol = "set volume output volume " + str(100)
# osascript.osascript(vol)
##############################################################



myVolume = 0
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        cv2.circle(img, (x1, y1), 12, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 12, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)
        # print(int(length))


        # Hand range 50 - 300
        # Volume range 0 - 100

        myVolume = np.interp(length, [50, 250], [minVol, maxVol])
        volBar = np.interp(length, [50, 250], [400, 150])
        volPer = np.interp(length, [50, 250], [0, 100])
        print(myVolume)


        target_volume = myVolume
        myVolume = "set volume output volume " + str(myVolume)
        osascript.osascript(myVolume)


        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f"{int(volPer)} %", (40, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Img", img)
    cv2.waitKey(1)