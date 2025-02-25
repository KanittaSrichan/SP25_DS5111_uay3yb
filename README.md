# Project Specific Setup

This repository is organized to make it easy to set up a new project environment on a fresh VM.

## Repository Organization

- **Base Directory:** Contains critical files such as `README.md`, `init.sh`, `Makefile`, and `requirements.txt`.
- **scripts/:** Contains one-off or supporting scripts (e.g., `install_chrome.sh`), which are used to install and configure necessary tools.
- **sample_data/:** Contains sample data files. For example, a sample `ygainers.csv` file is provided here to illustrate where project data should be placed.

## Actions

You can track the status of your tests with the badge below:

[![Feature Validation](https://github.com/KanittaSrichan/SP25_DS5111_uay3yb/actions/workflows/validations.yml/badge.svg)](https://github.com/KanittaSrichan/SP25_DS5111_uay3yb/actions/workflows/validations.yml)

## Setting Up the Environment

1. **VM Bootstrap:**
   - Update the OS package list:
     ```bash
     sudo apt update
     ```
   - Run the initialization script:
     ```bash
     ./init.sh
     ```

2. **Install Chrome Headless:**
   - Run the installation script:
     ```bash
     ./scripts/install_chrome.sh
     ```

3. **Set Up the Python Environment:**
   - Install the required packages:
     ```bash
     make update
     ```

4. **Testing the Setup:**
   - You can run tests with:
     ```bash
     make test_ygainers
     ```

---

### 3. Commit and Push Your Changes

```bash
git add -A
git commit -m "Update README with GitHub Actions badge"
git push
