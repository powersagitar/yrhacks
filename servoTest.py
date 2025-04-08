from adafruit_servokit import ServoKit
kit = ServoKit(channels=16, i2c=[1,3,5,10,13])
kit.I2C()
while True:
    a=input('enter:-')
    kit.servo[0].angle = int(a)   