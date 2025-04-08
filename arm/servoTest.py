from adafruit_servokit import ServoKit

# 1, 3, 5, 10 13
kit = ServoKit(channels=16)

while True:
    # p=input('pin: ')
    pin = input("pin: ")
    angle = input("value: ")

    kit.servo[int(pin)].angle = int(angle)
