from microbit import *

class obrazovka:
    def vypis(text):
        print(text)  # Výpis do terminálu počítače
        display.scroll(text)  # Výpis na displej Microbitu
