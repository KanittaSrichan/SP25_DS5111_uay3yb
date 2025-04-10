# test_system.py

import platform

def test_os_is_linux():
    # This test will fail if the OS is not Linux
    assert platform.system() == "Linux", f"Expected Linux, but got {platform.system()}"

def test_python_version():
    # This test will check that the Python version is 3.12
    expected_version = "3.12"
    actual_version = sys.version_info
    assert actual_version.major == 3 and actual_version.minor == 12, \
        f"Expected Python 3.12, but got Python {actual_version.major}.{actual_version.minor}"
