# test_system.py

import platform

def test_os_is_linux():
    # This test will fail if the OS is not Linux
    assert platform.system() == "Linux", f"Expected Linux, but got {platform.system()}"
