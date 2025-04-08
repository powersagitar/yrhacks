from cvzone.HandTrackingModule import HandDetector
import cv2
from adafruit_servokit import ServoKit
import time

# 1, 3, 5, 10 13
kit = ServoKit(channels=16)

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        hands1=hands[0]
        fingers1 = detector.fingersUp(hands1)
        print(fingers1)
        #thumb
        if fingers1[0]==0:
            print("down", end = ", ")
            kit.servo[0].angle = 10   
        elif fingers1[0]==1:
            print("up", end = ", ")
            kit.servo[0].angle = 0
        #index
        if fingers1[1]==0:
            print("down", end = ", ")
            kit.servo[1].angle = 10
        elif fingers1[1]==1:
            print("up", end = ", ")
            kit.servo[1].angle = 0
        #middle
        if fingers1[2]==0:
            print("down", end = ", ")
            kit.servo[2].angle = 10
        elif fingers1[2]==1:
            print("up", end = ", ")
            kit.servo[2].angle = 0
        #ring
        if fingers1[3]==0:
            print("down", end = ", ")
            kit.servo[3].angle = 10
        elif fingers1[3]==1:
            print("up", end = ", ")
            kit.servo[3].angle = 0
        #pinky
        if fingers1[4]==0:
            print("down")
            kit.servo[4].angle = 10
        elif fingers1[4]==1:
            print("up")
            kit.servo[4].angle = 0
      
            
    cv2.imshow("img",img)
    if cv2.waitKey(1)&0xFF==27:
        break
    elif cv2.waitKey(1)&0xFF=='0':
        kit.servo[0].angle = 0
        kit.servo[1].angle = 0
        kit.servo[2].angle = 0
        kit.servo[3].angle = 0
        kit.servo[4].angle = 0
        time.sleep(1)
        pass

cv2.cap.release()
cv2.destroyAllWindows()
