import asyncio
from bleak import BleakScanner

# async def main():
#     # Extend the scan duration to 10 seconds
#     devices = await BleakScanner.discover(timeout=10.0)
#     for d in devices:
#         # Print device address and name (if available)
#         print(f"Device: {d.address}, Name: {d.name}")

# asyncio.run(main())

import asyncio
from bleak import BleakClient

address = "2C:CF:67:A5:B3:F2"
MODEL_NBR_UUID = "0000110a-0000-1000-8000-00805f9b34fb"

async def main(address):
    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(MODEL_NBR_UUID)
        print("Model Number: {0}".format("".join(map(chr, model_number))))

asyncio.run(main(address))

# import asyncio
# from bleak import BleakClient

# address = "2C:CF:67:A5:B3:F2"  # Replace with the Bluetooth address of your Raspberry Pi

# async def main(address):
#     async with BleakClient(address) as client:
#         services = await client.get_services()
#         for service in services:
#             print(f"Service: {service.uuid}")
#             for characteristic in service.characteristics:
#                 print(f"  Characteristic: {characteristic.uuid}, Properties: {characteristic.properties}")

# asyncio.run(main(address))