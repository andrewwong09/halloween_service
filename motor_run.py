import RPi.GPIO as GPIO
import time

enable_pin = 26
pwr_pin = 4

def init_pins():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(enable_pin, GPIO.OUT)
    GPIO.setup(pwr_pin, GPIO.OUT)
    GPIO.output(enable_pin, GPIO.LOW)
    GPIO.output(pwr_pin, GPIO.HIGH)

def run_motor(time_s=4):
    GPIO.setwarnings(False)
    init_pins()
    GPIO.output(enable_pin, GPIO.HIGH)
    time.sleep(time_s)
    GPIO.output(enable_pin, GPIO.LOW)
    GPIO.cleanup()
