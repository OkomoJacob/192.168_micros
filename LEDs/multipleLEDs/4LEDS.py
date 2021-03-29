"""
Alternate the flashing of the LEDs,
Ensure you only use one GND for all GPIO connected pins.
"""
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time

tme = 0.3
#tme = float(input("Sleep for how many Seconds: "))
led1 = LED(4)
led2 = LED(17)
led3 = LED(27)
led4 = LED(22)

"""fucntion to alternate the blinking of LEDs"""
def alternateFlash():
    while True:
        led1.on()
        time.sleep(tme)
        led1.off()
        
        led2.on()
        time.sleep(tme)
        led2.off()
        
        led3.off()
        time.sleep(tme)
        led3.on()
        
        led1.on(); led2.on(); led3.on(); led4.on();
"""          
        led4.off()
        time.sleep(tme)
        led4.on()
        
        led1.off(); led2.off(); led3.off(); led4.off();
        led1.on(); led2.on(); led3.on(); led4.on();
"""
alternateFlash()