import asyncio
from classes.Thingy52Client import Thingy52Client
from utils.utility import scan, find

async def main():
    mac_address = "D3:70:53:C8:14:B1"
    discovered_devices = await scan()

    # find the BLE device
    device = find(discovered_devices, mac_address)

    thingy52 = Thingy52Client(device[0])
    await thingy52.connect()

    print(f"Connesso a {mac_address}. Inizio inferenza in tempo reale.")

    # save the data
    thingy52.save_to("movement_data")

    # inference
    await thingy52.receive_inertial_data()


if __name__ == "__main__":
    asyncio.run(main())