from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8

def test_requests_version():
    expected_version = "2.27"
    actual_version = requests_version()
    assert actual_version.startswith(expected_version) or actual_version > expected_version, \
        f"Expected requests version to be at least {expected_version}.x, but got {actual_version}"

def test_pytest_version():
    expected_version = "7.1"
    actual_version = pytest_version()
    assert actual_version.startswith(expected_version) or actual_version > expected_version, \
        f"Expected pytest version to be at least {expected_version}.x, but got {actual_version}"
