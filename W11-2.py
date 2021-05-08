import threading
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
mode = GPIO.getmode()

chan_list = [11,12]
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT)


def job():
    GPIO.output(26, GPIO.HIGH)
    time.sleep(1)
    print("HIGH")
        
while True:        
    t = threading.Thread(target = job)
    t.start()
#     for idx in range(10):
#         print("LOW")
#         time.sleep(2)
    t.join()
    GPIO.output(26, GPIO.LOW)
    time.sleep(1)
    print("LOW")
    
    print("Done!")
    # t.join()



