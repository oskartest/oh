import RPi.GPIO as GPIO
from time import sleep 
from gpiozero import Motor
import time
servoPin          = 12  
SERVO_MAX_DUTY    = 12 
SERVO_MIN_DUTY    = 3  
motor = Motor(forward=20, backward=21)
GPIO.setmode(GPIO.BOARD)       
GPIO.setup(servoPin, GPIO.OUT)

servo = GPIO.PWM(servoPin, 50) 
servo.start(0) 




def setServoPos(degree):
 
  if degree > 180:
    degree = 180


  duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
 
  print("Degree: {} to {}(Duty)".format(degree, duty))

  servo.ChangeDutyCycle(duty)





if __name__ == "__main__":  

  setServoPos(0)
  sleep(1) 

  setServoPos(90)
  sleep(1)

  setServoPos(50)
  sleep(1)


  setServoPos(120)
  sleep(1)

 
  setServoPos(180)
  sleep(1)

  servo.stop()

  GPIO.cleanup()
  while True:
    print('Forward')
    motor.forward(1)
    time.sleep(5)
    print('Backward')
    motor.Backward(1)
    time.sleep(5)
