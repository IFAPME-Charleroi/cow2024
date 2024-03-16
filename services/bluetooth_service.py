import asyncio
from bleak import BleakScanner, BleakClient

ADDRESS = "05:a1:cf:fb:cc:e4"
CHARACTERISTIC_UUID = "0000ae42-0000-1000-8000-00805f9b34fb"


def notification_handler(sender, data):
    """
    Cette fonction est appelée chaque fois qu'une notification est reçue
    pour la caractéristique à laquelle on est abonné.
    """
    print("Bouton pressé ! Données reçues :", data)


async def scan_and_connect():
    # Scan des périphériques BLE disponibles
    devices = await BleakScanner.discover()
    for device in devices:
        print(device)

    # Remplacez DEVICE_ADDRESS par l'adresse de votre bague
    device_address = "05:A1:CF:FB:CC:E4"
    async with BleakClient(device_address) as client:
        connected = await client.is_connected()
        print(f"Connected: {connected}")

        services = await client.get_services()
        for service in services:
            print(service)
        value = bytearray([0x01, 0x00])
        await client.write_gatt_char(CHARACTERISTIC_UUID, value, response=True)
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)

        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            # Assurez-vous de vous désabonner proprement
            await client.stop_notify(CHARACTERISTIC_UUID)
            print("Désabonnement effectué.")
# Exécute la fonction asynchrone
asyncio.run(scan_and_connect())
