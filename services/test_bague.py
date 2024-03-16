import asyncio
from bleak import BleakScanner, BleakClient

ADDRESS = "13:86:ab:aa:62:e8"

async def scan_and_connect():
    async with BleakClient(ADDRESS) as client:
        connected = await client.is_connected()
        print(f"Connected: {connected}")

        services = await client.get_services()
        for service in services:
            print(f"Service: {service}")
            print(f"Service UUID: {service.uuid}")
            for char in service.characteristics:
                print(f"    Characteristic: {char.uuid}")

# Exécute la fonction asynchrone
asyncio.run(scan_and_connect())