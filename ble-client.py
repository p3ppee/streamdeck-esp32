import asyncio
import subprocess
import os
from bleak import BleakScanner, BleakClient



esp32_addr = None



def gestisci_comando(sender, data):   #callback
  comando = data.decode()
  if comando == "SPOTIFY":
    print("comando spotify ricevuto")
    try:
      subprocess.Popen(["cmd", "/c", "start", "", "spotify:"])
    except:
      os.popen("spotify")
  elif comando == "DISCORD":
    print("comando discord ricevuto")
    try:
      subprocess.Popen(["cmd", "/c", "start", "", "discord:"])
    except:
      os.popen("discord")
  elif comando == "OTD":
    print("comando otd ricevuto")
    try:
      os.startfile(r'C:\Users\Fausto\Desktop\giochi\driver\OpenTabletDriver.UX.Wpf.exe')
    except:
      os.popen("otd-gui")
  elif comando == "ZEN":
    print("comando zen ricevuto")
    try:
      os.startfile(r"C:\Program Files\Zen Browser\zen.exe")
    except:
      os.popen("zen-browser")
  elif comando == "RE-PAIR":
    print("comando re-pair ricevuto")
  else:
    print("comando non riconosciuto")

async def trova_dispositivi():
  global esp32_addr
  dispositivi = await BleakScanner.discover(timeout = 5.0)
  for dispositivo in dispositivi:
    if dispositivo.name == "STREAMDECK-ESP32":
      print(dispositivo.address)
      esp32_addr = dispositivo.address

async def avvio():
  await trova_dispositivi()
  await main()

async def main():  #funzione main che permette di usare await senza def

  if esp32_addr is None: #controllo se ha trovato l'esp32, se non lo trova esce da main
      print("esp32 non trovato")
      return
  
  client = BleakClient(esp32_addr)
  await client.connect() #gestire disconnessione manualmente
  if client.is_connected:
    print("connesso")
  else:
    print("non connesso")
    
  servizi = client.services #tutti i servizi
  servizio = servizi.get_service("214ad5ab-1420-43c6-9fcf-95606d53ca24")    #prendo il servizio "utilizzato"
  if servizio is None:
    return
  caratteristica = servizio.get_characteristic("7cdc9eab-9927-4af8-8f56-6fd9e410cef0")   #caratterisctica spotify
  await client.start_notify(caratteristica, gestisci_comando)
  await asyncio.Event().wait()
  

asyncio.run(avvio())

