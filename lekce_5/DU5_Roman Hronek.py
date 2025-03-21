from microbit import sleep, pin14, pin15

def pocet_tiku_levy():
    surova_data_leva = pin14.read_digital()
    #zde napiste vas kod
    #scitejte tiky pro levy enkoder od zacatku behu progamu
    return #vratte soucet

def pocet_tiku_pravy():
    surova_data_prava = pin15.read_digital()
    #zde napiste vas kod
    #scitejte tiky pro pravy enkoder od zacatku behu progamu
    return #vratte soucet

def vypocti_rychlost_l(pocet_tiku_levy):
    sample_time = 200 #vzorkovací "frekvence"
    otacka = 20 #počet tiků za 1 otáčku
    start_lk = pocet_tiku_levy() #počáteční počet tiků
    start_time_l = time.tick.us() #čas začátku čtení tiků
    sleep(sample_time)
    end_lk = pocet_tiku_levy() #koncový počet tiků
    end_time_l = time.tick.us #čas konce čtení tiků
    tiky_l = end_lk - start_lk #změna počtu tiků
    cas_l = time.ticks_diff(end_time_l-start_time_l)/1000 #čas změny počtu tiků v sekundách
    omega = (tiky_l/otacka)*2*3.14159/cas_l #úhlová rychlost

    return #vratte rychlost v radianech za sekundu

if __name__ == "__main__":

    aktualni_rychlost = 0

    while True:
        print(pocet_tiku_levy(), pocet_tiku_pravy())
        aktualni_rychlost_l= vypocti_rychlost_l(pocet_tiku_levy)


        print(aktualni_rychlost)
        sleep(5)
