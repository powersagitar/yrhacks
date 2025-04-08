from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
            
    cv2.imshow("img",img)
    if cv2.waitKey(1)&0xFF==27:
        break

cv2.cap.release()
cv2.destroyAllWindows()
