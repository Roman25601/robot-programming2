from microbit import i2c, sleep

def init_motor():
    i2c.write(0x70, b'\x00\x01')
    i2c.write(0x70, b'\xE8\xAA')
    sleep(100)

def jed(strana, smer, rychlost):
    if strana == "leva":
        if smer == "dopredu":
            i2c.write(0x70, b‘\x05‘ + bytes([rychlost]))
        elif smer == "dozadu":
            i2c.write(0x70, b‘\x04‘ + bytes([rychlost]))

    if strana == "prava":
        if smer == "dopredu":
            i2c.write(0x70, b‘\x03‘ + bytes([rychlost]))
        elif smer == "dozadu":
            i2c.write(0x70, b‘\x02‘ + bytes([rychlost]))

if __name__ == "__main__":

    i2c.init()
    init_motor()
    jed("leva", "dopredu", 135)
    jed("prava", "dopredu", 135)
    sleep(1000)
    jed("leva", "dopredu", 0)
    jed("prava", "dopredu", 0)
    sleep(100)
    jed("leva", "dozadu", 135)
    jed("prava", "dozadu", 135)
    sleep(1000)
    jed("leva", "dozadu", 0)
    jed("prava", "dozadu", 0)

