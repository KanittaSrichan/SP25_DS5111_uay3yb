#!/bin/bash
# install_chrome.sh - Install Google Chrome Stable for headless use

set -e

echo "Downloading and installing Google Chrome Stable..."
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O /tmp/chrome.deb
sudo apt install /tmp/chrome.deb -y
rm /tmp/chrome.deb

echo "Google Chrome installation complete."
