from machine import I2C, Pin 
from bluetooth_test import invia_comando
import ssd1306
import time 

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

schermo = ssd1306.SSD1306_I2C(128, 64, i2c) 
pulsante1 = Pin(4, Pin.IN, Pin.PULL_UP)
pulsante2 = Pin(5, Pin.IN, Pin.PULL_UP)
pulsante3 = Pin(23, Pin.IN, Pin.PULL_UP)
pulsante4 = Pin(18, Pin.IN, Pin.PULL_UP)
pulsante5 = Pin(12, Pin.IN, Pin.PULL_UP)

#defining functions
def azione1():
    print("open spotify")
    invia_comando("SPOTIFY")
    schermo.fill(0)
    schermo.text("..OPENING SPOTIFY..", 0 ,0)
    schermo.show()
def azione2():
    print("open discord")
    invia_comando("DISCORD")
    schermo.fill(0)
    schermo.text("..OPENING DISCORD..", 0 ,0)
    schermo.show()
def azione3():
    print("open zen-browser")
    invia_comando("ZEN")
    schermo.fill(0)
    schermo.text("..OPENING ZEN-BROWSER..", 0 ,0)
    schermo.show()
def azione4():
    print("open otd")
    invia_comando("OTD")
    schermo.fill(0)
    schermo.text("..OPENING OTD..", 0 ,0)
    schermo.show()
def azione5():
    print("re-pair bluetooth")
    schermo.fill(0)
    schermo.text("..PAIRING..", 0 ,0)
    schermo.show()


#inizializing OLED display
schermo.fill(0)
schermo.text("MY STREAM DECK", 0, 0)
schermo.text("System Ready!", 0, 20)
schermo.show()



while True:
    if pulsante1.value() == 0 :
        azione1()
    elif pulsante2.value() == 0 :
        azione2()
    elif pulsante3.value() == 0 :
        azione3()
    elif pulsante4.value() == 0 :
        azione4()
    elif pulsante5.value() == 0 :
        azione5()

    time.sleep(1.0)