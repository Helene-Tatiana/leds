from machine import Pin
import utime

LED_R = Pin(15, Pin.OUT) 'led rouge'
LED_G = Pin(13, Pin.OUT) 'led verte'
LED_B = Pin(12, Pin.OUT) 'led bleue'

BP1 = Pin(18, Pin.OUT) 'bouton poussoir 1'
BP2 = Pin(19, Pin.PULL_DOWN) 'bouton poussoir 2'

while True:
    if BP1.value():
        LED_R.toggle()
        utime.sleep(1)
    elif BP1.value(): 
        LED_G.toggle()
        utime.sleep(1)
    elif BP1.value(): 
        LED_B.toggle()
        utime.sleep(1)
    elif BP2.value():
        LED_R.off()
        LED_G.off()
        LED_B.off()
        utime.sleep(0)

    