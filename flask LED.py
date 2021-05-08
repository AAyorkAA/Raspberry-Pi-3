import RPi.GPIO as GPIO
import time
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/a')
def led1():
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()

    chan_list = [11,12]
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)

    GPIO.output(26, GPIO.HIGH)
    return 'LED_HIGH!'
    
@app.route('/b')
def led2():
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()

    chan_list = [11,12]
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)

    GPIO.output(26, GPIO.LOW)
    return 'LED_LOW!'


@app.route('/c')
def led3():
    GPIO.setmode(GPIO.BCM)
    mode = GPIO.getmode()

    chan_list = [11,12]
    GPIO.setwarnings(False)
    GPIO.setup(26, GPIO.OUT)
    
    def job():
        GPIO.output(26, GPIO.HIGH)
        time.sleep(1)
    while True:
        t = threading.Thread(target = job)
        t.start()
        t.join()
        GPIO.output(26, GPIO.LOW)
        time.sleep(1)
    return 'LED_HIGH_LOW!'


if __name__ == '__main__':
    app.run()
