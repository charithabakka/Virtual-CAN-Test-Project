#!/bin/bash

# Step 1: Setup Virtual CAN Interface
echo "🔧 Setting up virtual CAN interface (vcan0)..."
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan 2>/dev/null
sudo ip link set up vcan0
ip a show vcan0 | grep vcan0

# Step 2: Activate virtual environment
echo "🐍 Activating Python virtual environment..."
source venv/bin/activate

# Step 3: Start ECU Simulator in a background terminal
echo "🚗 Starting ECU Simulator..."
gnome-terminal -- bash -c "cd Virtual-CAN-Test-Project && source venv/bin/activate && python3 ecu_simulator/ecu_simulator.py; exec bash"

# Step 4: Start Test Script in a background terminal
echo "🧪 Starting Test Script..."
gnome-terminal -- bash -c "cd Virtual-CAN-Test-Project && source venv/bin/activate && python3 test_scripts/test_display_response.py; exec bash"

echo "✅ All components started!"
