# VM Setup for Data Science Projects

## Introduction

Welcome to our data science project setup guide. This repository provides scripts and instructions to automate the setup of a Virtual Machine (VM) for data science tasks, focusing on creating a reproducible environment that facilitates data collection using a headless Chrome browser and analysis using Python.

[![Feature Validation](https://github.com/KanittaSrichan/SP25_DS5111_uay3yb/actions/workflows/validations.yml/badge.svg)](https://github.com/KanittaSrichan/SP25_DS5111_uay3yb/actions/workflows/validations.yml)

## Learning Objectives

- Automate VM setup to ensure quick and reproducible deployment.
- Install essential tools like Google Chrome in headless mode for data scraping.
- Establish a Python development environment using virtual environments and a Makefile.

## Repository Structure

/ |-- README.md  
|-- init.sh  
|-- Makefile  
|-- requirements.txt  
|-- scripts/  
| |-- install_chrome.sh  
|-- sample_data/  
| |-- ygainers.csv

## Setup Instructions

### Initial VM Setup

1. **Update and Install Essential Tools:**
   - Manually update your VM's package list to ensure you have the latest versions:
     ```bash
     sudo apt update
     ```
   - Execute the `init.sh` script to automate the installation of Make, Python environment tools, and other utilities:
     ```bash
     ./init.sh
     ```

2. **Configure Git and SSH:**
   - Set up Git credentials and generate an SSH key following the lab's previous instructions.
   - Clone this repository to synchronize all project files locally:
     ```bash
     git clone [your-repository-url]
     ```

### Project-Specific Setup

1. **Headless Chrome Installation:**
   - Deploy the headless Chrome browser using the `install_chrome.sh` script for automated data scraping tasks:
     ```bash
     ./scripts/install_chrome.sh
     ```

2. **Python Environment and Dependencies:**
   - Use the Makefile to set up your Python virtual environment and install dependencies listed in `requirements.txt`:
     ```bash
     make update
     ```
   - Verify the setup by running a test command to check Chrome's headless operation:
     ```bash
     make test_ygainers
     ```

3. **Verify Repository Structure:**
   - Confirm the setup and organization of your project using the `tree` command, excluding the virtual environment directory:
     ```bash
     tree <your project-repo> -I env
     ```

## Troubleshooting

If you encounter issues during the setup, consider the following:
- Ensure scripts are executable: `chmod +x *.sh`.
- Verify Python and dependencies are installed correctly.
- Check network settings if there are issues with package installations.

## Contributing

To contribute to this repository, fork the project, make your changes, and submit a pull request. Ensure your contributions adhere to established coding standards and include proper documentation.

## FAQs

**Q: What if the `make update` command fails?**  
**A:** Check that Python and `make` are installed correctly, and review `requirements.txt` for any incompatible package versions.

**Q: How do I update scripts for a new OS version?**  
**A:** Update the package installation commands in the `init.sh` script according to new OS requirements and test thoroughly.

## Contact

For further assistance or inquiries, please contact uay3yb@virginia.edu
