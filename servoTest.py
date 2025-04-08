from adafruit_servokit import ServoKit
# 1, 3, 5, 10 13
kit = ServoKit(channels=16)

while True:
    a=input('enter:-')
    kit.servo[0].angle = int(a)   