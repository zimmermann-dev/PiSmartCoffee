from time import sleep

from gpiozero import LED

powerbtn = LED(4)
brewonecupbtn = LED(3)


def brew():
    sleep(65)

    if brewonecupbtn.value == 0:
        brewonecupbtn.toggle()
        sleep(10)
        power()
    else:
        exit()


def power():
    if powerbtn.value == 0:
        powerbtn.toggle()
        sleep(5)
        brew()
    else:
        powerbtn.toggle()
        sleep(2)
        exit()
