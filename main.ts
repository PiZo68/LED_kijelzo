let magassag = 0
basic.forever(function () {
    basic.clearScreen()
    magassag = randint(0, 4)
    for (let index = 0; index <= magassag; index++) {
        led.plot(0, 4 - index)
    }
    magassag = randint(0, 4)
    for (let index = 0; index <= magassag; index++) {
        led.plot(1, 4 - index)
    }
    magassag = randint(0, 4)
    for (let index = 0; index <= magassag; index++) {
        led.plot(2, 4 - index)
    }
    magassag = randint(0, 4)
    for (let index = 0; index <= magassag; index++) {
        led.plot(3, 4 - index)
    }
    magassag = randint(0, 4)
    for (let index = 0; index <= magassag; index++) {
        led.plot(4, 4 - index)
    }
    basic.pause(50)
})
