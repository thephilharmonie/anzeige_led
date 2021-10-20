def led_array(dist):
    led = 0

    for i in range(dist):
        led = led + (pow(10, i))

    zeros = pow(10, (16 - dist))

    end_value = led * zeros

    ledpattern = str(end_value)

    reverse_pattern = ledpattern[::-1]

    print(reverse_pattern)

dist= 8
led_array(dist)

