# Project Specific Setup

This repository is organized to make it easy to set up a new project environment on a fresh VM.

## Repository Organization

- **Base Directory:** Contains critical files such as `README.md`, `init.sh`, `Makefile`, and `requirements.txt`.
- **scripts/:** Contains one-off or supporting scripts (e.g., `install_chrome.sh`), which are used to install and configure necessary tools.
- **sample_data/:** Contains sample data files. For example, a sample `ygainers.csv` file is provided here to illustrate where project data should be placed.

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
   - Verify by running:
     ```bash
     google-chrome-stable --headless --disable-gpu --dump-dom https://example.com
     ```
     (Ignore any UPower warnings if the HTML output for example.com appears.)

3. **Set Up the Python Environment:**
   - Install the required packages:
     ```bash
     make update
     ```
     (This creates a virtual environment and installs packages listed in `requirements.txt`, such as `pandas` and `lxml`.)

4. **Testing the Setup:**
   - A sample Makefile target (e.g., for processing or testing) may be available.
   - For example, a target to generate `ygainers.csv` from sample data might be available. You can run it with:
     ```bash
     make test_ygainers
     ```
     (This target should produce output saved to `sample_data/ygainers.csv`.)

Following these steps will ensure that the repository is well-organized and that the setup instructions are clear. This will make it easy for anyone, including me in the future or a new team member, to bootstrap a new VM and get the project up and running quickly.

---

### 3. Commit and Push Your Changes

After updating your files and README, stage and commit your changes:

```bash
git add -A
git commit -m "Organize repository: add scripts/ and sample_data/ directories, update README"
git push



### Actions
[![Feature Validation](https://github.com/KanittaSrichan/SP25_DS5111_uay3yb/actions/workflows/validations.yml/badge.svg)](https://github.com/KanittaSrichan/SP25_DS5111_uay3yb/actions/workflows/validations.yml)
