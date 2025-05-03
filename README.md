# Virtual CAN Test Project

## Overview
This project simulates a simple ECU behavior using virtual CAN interfaces (SocketCAN) and tests it using open-source tools in Python.

## Tools Used
- python-can
- cantools
- pytest
- SocketCAN
- Git/GitHub

## Project Structure
- `dbc_files/`: Contains mock DBC files.
- `test_scripts/`: Python scripts to test ECU behavior.
- `ecu_simulator/`: Mock ECU logic that listens and responds to CAN messages.
- `logs/`: Log outputs and test reports.
- `utils/`: Helper functions and tools.

## How to Run
1. Set up virtual CAN interface on Linux:
    ```bash
    sudo modprobe vcan
    sudo ip link add dev vcan0 type vcan
    sudo ip link set up vcan0
    ```

2. Run the ECU simulator.

3. Execute the test scripts.
