from microbit import sleep, pin14, pin15, _thread
pl = 0
pp = 0
def pocet_tiku_levy():
    global pl
    old_leva = pin14.read_digital()
    while True:
        new_leva = pin14.read_digital()
        if new_leva != old_leva
            pl += 1
            old_leva = new_leva
        sleep(2)

def pocet_tiku_pravy():
    global pp
    old_prava = pin15.read_digital()
    while True:
        new_prava = pin15.read_digital()
        if new_prava != old_prava
            pp += 1
            old_prava = new_prava
        sleep(2)

if __name__ == "__main__":
    _thread.start_new_thread(pocet_tiku_levy())
    _thread.start_new_thread(pocet_tiku_pravy())

while True:
    print(pl, pp)
    sleep(100)
