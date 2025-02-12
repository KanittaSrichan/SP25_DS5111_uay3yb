#!/bin/bash
# This script sets up the base tools on your VM

set -e  # Stop the script if any command fails

echo "Updating package list..."
sudo apt update

echo "Installing make..."
sudo apt install make -y

echo "Installing Python3.12 venv support..."
sudo apt install python3.12-venv -y

echo "Installing tree..."
sudo apt install tree -y

echo "Initialization complete."
