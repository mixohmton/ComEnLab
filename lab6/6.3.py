import RPi.GPIO as GPIO
import time
 
sw = 22
count = 0
LED = 18
LED_State = False
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
 
try:
    GPIO.output(LED, 0)
    while True:
        if GPIO.wait_for_edge(sw,GPIO.FALLING):
            LED_State = not(LED_State)
            GPIO.output(LED,LED_State)
            print(f"LED => {'ติด' if LED_State else 'ดับนะจ้ะ'}")
            time.sleep(0.2)
except KeyboardInterrupt:
    GPIO.cleanup()
print("\nBye...")
