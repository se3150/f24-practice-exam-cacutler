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
        def it_recharges_with_a_positive_amount(partially_charged_battery):
            assert partially_charged_battery.mCharge == 70
            return_value = partially_charged_battery.recharge(20)
            assert partially_charged_battery.mCharge == 90
            assert return_value
        def it_does_not_recharge_with_a_negative_amount(partially_charged_battery):
            assert partially_charged_battery.mCharge == 70
            return_value = partially_charged_battery.recharge(-5)
            assert partially_charged_battery.mCharge != 65
            assert partially_charged_battery.mCharge == 70
            assert not return_value
        def it_does_not_recharge_with_a_zero_amount(partially_charged_battery):
            assert partially_charged_battery.mCharge == 70
            return_value = partially_charged_battery.recharge(0)
            assert partially_charged_battery.mCharge == 70
            assert not return_value
        def it_does_not_exceed_capacity_on_recharge(partially_charged_battery):
            assert partially_charged_battery.mCharge == 70
            return_value = partially_charged_battery.recharge(31)
            assert partially_charged_battery.mCharge != 101
            assert partially_charged_battery.mCharge == 100
            assert return_value
    def describe_drain():
        # your test cases here
        pass