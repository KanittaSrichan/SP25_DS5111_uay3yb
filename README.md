# SP25_DS5111_uay3yb
Spring 2025 Software and Automation Skills




# VM Bootstrap and Setup Guide

This section describes how to set up a new VM for this (or any similar) project.

## 1. Initial VM Setup

Before running any of our scripts, you must perform some manual steps on a fresh VM:

1. **Update the OS package list:**
   Run the following command in the terminal:
   ```bash
   sudo apt update






# Project Specific Setup

This section explains how to set up the project-specific environment, including installing Chrome Headless, setting up the Python virtual environment, and testing key functionalities.

## 1. Install Chrome Headless

Run the script from the last lab to install Google Chrome in headless mode:

```bash
./scripts/install_chrome.sh







## Testing Chrome Headless

After installing Google Chrome, verify that it works in headless mode by running:

```bash
google-chrome-stable --headless --disable-gpu --dump-dom https://example.com
