from cvzone.HandTrackingModule import HandDetector
import cv2

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
        elif fingers1[0]==1:
            print("up", end = ", ")
        #index
        if fingers1[1]==0:
            print("down", end = ", ")
        elif fingers1[1]==1:
            print("up", end = ", ")
        #middle
        if fingers1[2]==0:
            print("down", end = ", ")
        elif fingers1[2]==1:
            print("up", end = ", ")
        #ring
        if fingers1[3]==0:
            print("down", end = ", ")
        elif fingers1[3]==1:
            print("up", end = ", ")
        #pinky
        if fingers1[4]==0:
            print("down")
        elif fingers1[4]==1:
            print("up")
      
            
    cv2.imshow("img",img)
    if cv2.waitKey(1)&0xFF==27:
        break

cv2.cap.release()
cv2.destroyAllWindows()
