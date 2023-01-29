import pytest

# scope decides if a fixture will once and be used by all the test that needs it, or run with each test one after the other.

# marks provide some meta data on the test. it has xfail, skip etc
# pytest -rP to get more information when we run test
# coverage run -m pytest:  running pytest with coverage
@pytest.fixture(scope="session")
def text_fixture1():
    print("run once")
    return 1
