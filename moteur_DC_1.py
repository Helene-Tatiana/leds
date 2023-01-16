from machine import Pin
import time


IN_1 = Pin(1, Pin.OUT)
IN_2 = Pin(2, Pin.OUT)
ENA_1 = Pin(16, Pin.OUT)

def clockwise():
    IN_1.value(1)
    IN_2.value(0)
    ENA_1.value(1)
    print('clockwise')

def counterclockwise():
    IN_1.value(0)
    IN_2.value(1)
    ENA_1.value(1)
    print('counterclockwise')
    time.sleep_ms(15000)
    rotate()
    
def rotate():
    clockwise()
    time.sleep_ms(15000)
    counterclockwise()
    
rotate()




