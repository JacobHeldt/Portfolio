import cv2
import numpy as np
import time
import PoseModule as pm

cap = cv2.VideoCapture(0)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    # img = cv2.imread("AITrainer/test.jpg")
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        # detector.findAngle(img, 11, 13, 15)
        per = np.interp(angle, (50, 140), (100, 0))
        bar = np.interp(angle, (50, 140), (100, 650))
        # print(angle, per)

        # Check for the dumbbell curls
        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)

        # Draw Bar
        cv2.rectangle(img, (1100, 100), (1175, 650), color, 3)
        cv2.rectangle(img, (1100, int(bar)), (1175, 650), color, cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (1075, 75), cv2.FONT_HERSHEY_SIMPLEX, 3, color, 5)

        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_SIMPLEX, 7, (255, 0, 0), 20)

        cTime = time.time()
        fps = 1/(cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (40, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 4)

    cv2.imshow("Image", img)
    cv2.waitKey(1)