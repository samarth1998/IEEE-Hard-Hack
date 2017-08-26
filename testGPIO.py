#GPIO Library===================================
import time
from gpio_96boards import GPIO
GPA = GPIO.gpio_id('GPIO_A')
GPB = GPIO.gpio_id('GPIO_B')
GPC = GPIO.gpio_id('GPIO_C')
GPD = GPIO.gpio_id('GPIO_D')

def gpio_h(gpid):
    pins = (
    (gpid, 'out'),)
    with GPIO(pins) as gpio:
        gpio.digital_write(gpid, GPIO.HIGH)
def gpio_l(gpid):
    pins = (
    (gpid, 'out'),)
    with GPIO(pins) as gpio:
        gpio.digital_write(gpid, GPIO.LOW)

def gpio_r(gpid):
    pins = (
    (gpid, 'in'),)
    with GPIO(pins) as gpio:
        data = gpio.digital_read(gpid)
    return data

#gpio_h(GPC)
#time.sleep(1)
#gpio_l(GPC)
#gpio_r(GPA)
