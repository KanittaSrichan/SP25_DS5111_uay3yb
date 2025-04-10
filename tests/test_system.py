# test_system.py

import platform
import platform
import sys


def test_os_is_linux():
    # This test will fail if the OS is not Linux
    assert platform.system() == "Linux", f"Expected Linux, but got {platform.system()}"

import sys

def test_python_version():
    # This test will check that the Python version is either 3.12 or 3.13
    expected_major_version = 3
    expected_minor_versions = [12, 13]  # We accept both 3.12 and 3.13

    actual_version = sys.version_info
    assert actual_version.major == expected_major_version, \
        f"Expected Python 3.x, but got Python {actual_version.major}.{actual_version.minor}"

    assert actual_version.minor in expected_minor_versions, \
        f"Expected Python 3.12 or 3.13, but got Python {actual_version.major}.{actual_version.minor}"
