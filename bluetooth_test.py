import bluetooth
from micropython import const
_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)


#defining conn_handle to make it a global variable
conn_handle = None
#defining functions
def gestisci_eventi(evento, dati):
    global conn_handle
    if evento == _IRQ_CENTRAL_CONNECT:
        conn_handle, addr_type, addr = dati
    elif evento == _IRQ_CENTRAL_DISCONNECT:
        conn_handle = None
    
def invia_comando(comando):
    if conn_handle is not None:
        ble.gatts_write(handle_comandi, comando.encode())
        ble.gatts_notify(conn_handle, handle_comandi)
        
    else:
        print("non connesso al pc")

#ble stands for bluetooth low energy 
ble = bluetooth.BLE()
ble.active(True)
ble.config(gap_name="STREAMDECK-ESP32")
nome = ("STREAMDECK-ESP32")
dati = nome.encode()

ble.irq(handler=gestisci_eventi)

pacchetto_nome = bytearray([len(dati) + 1, 0x09]) + bytearray(dati)
flags = bytearray([0x02, 0x01, 0x06])

adv_data = flags + pacchetto_nome 


UUID_SERVIZIO = bluetooth.UUID("214ad5ab-1420-43c6-9fcf-95606d53ca24")
UUID_COMANDI = bluetooth.UUID("7cdc9eab-9927-4af8-8f56-6fd9e410cef0")

SERVIZIO = (
    UUID_SERVIZIO,
    (
        (UUID_COMANDI, bluetooth.FLAG_READ | bluetooth.FLAG_NOTIFY),
    ),
)
servizi = ble.gatts_register_services((SERVIZIO,))
handle_comandi = servizi[0][0]

ble.gap_advertise(100000, adv_data=adv_data)