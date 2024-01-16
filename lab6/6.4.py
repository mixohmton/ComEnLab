import RPi.GPIO as GPIO
import time

sw = 22
LED_R = 18
LED_G = 17
LED_B = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)

colors = [
    [0, 0, 0],  
    [0, 0, 1],  
    [0, 1, 0],  
    [0, 1, 1],  
    [1, 0, 0], 
    [1, 0, 1],  
    [1, 1, 0],
    [1, 1, 1]    
]

current_color = 0

try:
    while True:
        GPIO.wait_for_edge(sw, GPIO.FALLING)

        current_color = (current_color + 1) % len(colors)

        for i in range(3):
            GPIO.output([LED_R, LED_G, LED_B][i], colors[current_color][i])

        print(f"RGB LED => {'Off' if all(x == 0 for x in colors[current_color]) else 'Blue' if colors[current_color][2] else 'Green' if colors[current_color][1] else 'Red'}")

        GPIO.wait_for_edge(sw, GPIO.RISING) 
        time.sleep(0.2) 

except KeyboardInterrupt:
    GPIO.cleanup()

print("\nBye...")
