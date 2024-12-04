import pytest
from battery import Battery
from unittest.mock import Mock
todo = pytest.mark.skip(reason='todo: pending spec')
@pytest.fixture
def charged_battery():
    return Battery(100)
@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b
def describe_Battery():
    def describe_recharge():
        # your test cases here
        pass
    def describe_drain():
        # your test cases here
        pass