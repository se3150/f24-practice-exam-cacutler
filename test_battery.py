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
            assert partially_charged_battery.getCharge() == 70
            return_value = partially_charged_battery.recharge(20)
            assert partially_charged_battery.getCharge() == 90
            assert return_value
        def it_does_not_recharge_with_a_negative_amount(partially_charged_battery):
            assert partially_charged_battery.getCharge() == 70
            return_value = partially_charged_battery.recharge(-5)
            assert partially_charged_battery.getCharge() != 65
            assert partially_charged_battery.getCharge() == 70
            assert not return_value
        def it_does_not_recharge_with_a_zero_amount(partially_charged_battery):
            assert partially_charged_battery.getCharge() == 70
            return_value = partially_charged_battery.recharge(0)
            assert partially_charged_battery.getCharge() == 70
            assert not return_value
        def it_does_not_exceed_capacity_on_recharge(partially_charged_battery):
            assert partially_charged_battery.getCharge() == 70
            assert partially_charged_battery.getCapacity() == 100
            return_value = partially_charged_battery.recharge(31)
            assert partially_charged_battery.getCharge() != 101
            assert partially_charged_battery.getCharge() == 100
            assert return_value
        def external_monitor_notifies_recharge():
            external_monitor_mock = Mock()
            b = Battery(100, external_monitor=external_monitor_mock)
            b.mCharge = 70
            b.recharge(20)
            external_monitor_mock.notify_recharge.assert_called_once_with(90)
    def describe_drain():
        # your test cases here
        def it_drains_with_a_positive_amount(charged_battery):
            assert charged_battery.getCharge() == 100
            return_value = charged_battery.drain(50)
            assert charged_battery.getCharge() == 50
            assert return_value
        def it_does_not_drain_with_a_negative_amount(charged_battery):
            assert charged_battery.getCharge() == 100
            return_value = charged_battery.drain(-5)
            assert charged_battery.getCharge() == 100
            assert not return_value 
        def it_does_not_drain_with_a_zero_amount(charged_battery):
            assert charged_battery.getCharge() == 100
            return_value = charged_battery.drain(0)
            assert charged_battery.getCharge() == 100
            assert not return_value
        def it_does_not_drain_past_the_full_capacity(charged_battery):
            assert charged_battery.getCharge() == 100
            return_value = charged_battery.drain(101)
            assert charged_battery.getCharge() == 0
            assert return_value
        def external_monitor_notifies_drain():
            external_monitor_mock = Mock()
            b = Battery(100, external_monitor=external_monitor_mock)
            b.drain(30)
            external_monitor_mock.notify_drain.assert_called_once_with(70)