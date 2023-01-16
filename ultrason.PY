from hcsr04 import HCSR04
sensor = HCSR04(trigger_pin=3, echo_pin=4)
distance = sensor.distance_cm()
print('Distance:', distance, 'cm')
