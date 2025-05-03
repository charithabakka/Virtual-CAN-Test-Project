import can
import time

def send_and_check(ignition, light):
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

    # Send input
    msg = can.Message(arbitration_id=0x101, data=[int(ignition), int(light)], is_extended_id=False)
    bus.send(msg)
    print(f"Sent test: Ignition={ignition}, Light={light}")

    # Wait and receive response
    response = bus.recv(timeout=1)
    if response and response.arbitration_id == 0x201:
        display_state = "ON" if response.data[0] else "OFF"
        print(f"Display Response: {display_state}")
        return display_state
    else:
        print("No response received.")
        return None

if __name__ == "__main__":
    # Run test case: ignition ON, light LOW → Expect display ON
    result = send_and_check(ignition=True, light=True)
