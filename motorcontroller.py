import RPi.GPIO as GPIO

class MotorController():

    def __init()__(self, mouth_open_pin, mouth_close_pin, body_towards_pin, body_away_pin ):
        
        self.mouth_open_pin = mouth_open_pin
        self.mouth_close_pin = mouth_close_pin
        self.body_towards_pin = body_towards_pin
        self.body_away_pin = body_away_pin
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.mouth_open_pin, GPIO.OUT,  initial=GPIO.LOW)
        GPIO.setup(self.mouth_close_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.body_towards_pin, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.body_away_pin, GPIO.OUT, initial=GPIO.LOW)
        
    def move_mouth(open):
        GPIO.set(self.mouth_open_pin, open)
        GPIO.set(self.mouth_close_pin, not open)
    
    def move_body(towards):
        GPIO.set(self.body_towards_pin, towards)
        GPIO.set(self.body_away_pin, not towards)
        
    def close():
        GPIO.cleanup()
   
