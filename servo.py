from time import sleep, time
from adafruit_servokit import ServoKit


kit = ServoKit(channels=16)
#kit.servo[0].angle = 180
#sleep(1)
#kit.servo[0].angle = 0
#sleep(1)
#kit.servo[0].angle = 90
kit.continuous_servo[1].throttle = 0.1
print(1)
sleep(2)
kit.continuous_servo[1].throttle = -1
kit.continuous_servo[1].throttle = 0

