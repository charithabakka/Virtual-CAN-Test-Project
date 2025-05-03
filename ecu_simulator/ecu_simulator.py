import can
import time

def run_simulator():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    print("Mock ECU started. Listening on vcan0...")

    while True:
        msg = bus.recv()
        if msg is None:
            continue

        if msg.arbitration_id == 0x101:
            ignition_on = bool(msg.data[0])
            light_low = bool(msg.data[1])

            print(f"Received: Ignition={ignition_on}, Light={light_low}")

            if ignition_on and light_low:
                # Send display ON response
                response = can.Message(arbitration_id=0x201, data=[1], is_extended_id=False)
            else:
                # Send display OFF
                response = can.Message(arbitration_id=0x201, data=[0], is_extended_id=False)

            bus.send(response)
            print(f"Sent response: Display={'ON' if response.data[0] else 'OFF'}")

if __name__ == "__main__":
    run_simulator()
