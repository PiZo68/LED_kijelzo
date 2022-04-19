magassag = 0

def on_forever():
    global magassag
    basic.clear_screen()
    magassag = randint(0, 4)
    index = 0
    while index <= magassag:
        led.plot(0, 4 - index)
        index += 1
    magassag = randint(0, 4)
    index2 = 0
    while index2 <= magassag:
        led.plot(1, 4 - index2)
        index2 += 1
    magassag = randint(0, 4)
    index3 = 0
    while index3 <= magassag:
        led.plot(2, 4 - index3)
        index3 += 1
    magassag = randint(0, 4)
    index4 = 0
    while index4 <= magassag:
        led.plot(3, 4 - index4)
        index4 += 1
    magassag = randint(0, 4)
    index5 = 0
    while index5 <= magassag:
        led.plot(4, 4 - index5)
        index5 += 1
    basic.pause(50)
basic.forever(on_forever)
