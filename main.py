import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

PIN_DATA = 16
PIN_LATCH = 20
PIN_CLOCK = 21

GPIO.setwarnings(False)
GPIO.setup(PIN_DATA, GPIO.OUT)
GPIO.setup(PIN_LATCH, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)


def led_array(dist):
    ones = 0
    for i in range(dist):
        ones = ones + (pow(10, i))
    zeros = pow(10, (16 - dist))
    end_value = ones * zeros
    ledpattern = str(end_value)
    reverse_pattern = ledpattern[::-1]
    print(reverse_pattern)  # led Status zur Überprüfung

    GPIO.output(PIN_LATCH, 0)
    for x in range(16):
        GPIO.output(PIN_DATA, int(reverse_pattern[x]))
        # print(int(ledpattern[x]))
        GPIO.output(PIN_CLOCK, 1)
        GPIO.output(PIN_CLOCK, 0)

    GPIO.output(PIN_LATCH, 1)

#------------------------------------
# Beispiel: Angenommen die Distanze (dist) würde 4 Einheiten betragen:

dist= 4

led_array(dist)