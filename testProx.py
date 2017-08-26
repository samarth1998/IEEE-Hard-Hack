#GPIO Library===================================
import time
from gpio_96boards import GPIO
GPA = GPIO.gpio_id('GPIO_A')
GPB = GPIO.gpio_id('GPIO_B')
GPC = GPIO.gpio_id('GPIO_C')
GPD = GPIO.gpio_id('GPIO_D')
gpioread = 0
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
#    pins = (
#    (gpid, 'in'),)
    with GPIO(pinsread) as gpio:
        data = gpio.digital_read(gpid)
    return data
def setupRead(gpid):
    global pinsread
    pinsread = (
    (gpid, 'in'),)
#gpio_h(GPC)
#time.sleep(1)
#gpio_l(GPC)
#gpio_r(GPA)
#GPIO Library Ends======================================

#Trigger connected to GPIO_A, Echo connected to GPIO_B
#Set GPIO Pins
trig = GPA
echo = GPB
setupRead(echo)
def getDistance():
    #Set trigger to high
    gpio_h(trig)

    #Set trigger after 0.01ms to LOW
    time.sleep(0.00001)
    gpio_l(trig)

    StartTime = time.time()
    StopTime = time.time()

    #Save StartTime
    while gpio_r(echo) == 0:
        StartTime = time.time()
    #Save time of arrival
    while gpio_r(echo) == 1:
        StopTime = time.time()

    #Time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    #Multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    if distance > 1000:
        return 1000
    return distance

if __name__ == '__main__':
    dist = getDistance()
    print dist
    while True:
        try:
            print getDistance()
            time.sleep(1)
        except:
            print 'Balls'
            time.sleep(1)
            continue
