import asyncio
import subprocess
from bleak import BleakScanner, BleakClient

esp32_addr = None

def callback(sender, data):
  print("Comando ricevuto:", data.decode())

def gestisci_comando(sender, data):
  comando = data.decode()
  if comando == "SPOTIFY":
    print("comando spotify ricevuto")
    subprocess.Popen(["cmd", "/c", "start", "", "spotify:"])
  elif comando == "DISCORD":
    print("comando discord ricevuto")
    subprocess.Popen(["cmd", "/c", "start", "", "discord:"])
  elif comando == "OTD":
    print("comando otd ricevuto")
  elif comando == "ZEN":
    print("comando zen ricevuto")
  elif comando == "RE-PAIR":
    print("comando re-pair ricevuto")
  else:
    print("comando non riconosciuto")

async def trova_dispositivi():
  dispositivi = await BleakScanner.discover(timeout = 5.0)
  for dispositivo in dispositivi:
    if dispositivo.name == "STREAMDECK-ESP32":
      print(dispositivo.address)
      esp32_addr = dispositivo.address

client = BleackClient(esp32_addr)
await client.connect() #gestire disconnessione manualmente
if client.is_connected:
  print("connesso")
else:
  print("non connesso")
  
servizi = await client.get_service() #tutti i servizi
servizo = servizi.get_service("214ad5ab-1420-43c6-9fcf-95606d53ca24")    #prendo il servizio "utilizato"
caratteristica = servizi.get_characteristic("7cdc9eab-9927-4af8-8f56-6fd9e410cef0")   #caratterisctica spotify
await client.start_notify(caratteristica, callback)

asyncio.run(trova_dispositivo())

