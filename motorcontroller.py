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
        
    def open_mouth():
        GPIO.set(self.mouth_open_pin, True)
        GPIO.set(self.mouth_close_pin, False)
    
    def close_mouth():
        GPIO.set(self.mouth_open_pin, False)
        GPIO.set(self.mouth_close_pin, True)
    
    def body_towards():
        GPIO.set(self.body_towards_pin, True)
        GPIO.set(self.body_away_pin, False)
        
    def body_away():
        GPIO.set(self.body_towards_pin, False)
        GPIO.set(self.body_away_pin, True)
                 
    def close():
        GPIO.cleanup()
   
