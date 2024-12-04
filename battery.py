class Battery:
    def __init__(self, capacity, external_monitor=None):
        self.mCapacity = capacity
        self.mCharge = capacity
        self.external_monitor = external_monitor  # Dependency for monitoring
    def getCapacity(self):
        return self.mCapacity
    def getCharge(self):
        return self.mCharge
    def recharge(self, amount):
        if amount > 0 and self.mCharge < self.mCapacity:
            self.mCharge += amount
            if self.mCharge > self.mCapacity:
                self.mCharge = self.mCapacity
            # Notify external monitor about recharge
            if self.external_monitor:
                self.external_monitor.notify_recharge(self.mCharge)
            return True
        return False
    def drain(self, amount):
        if amount > 0 and self.mCharge > 0:
            self.mCharge -= amount
            if self.mCharge < 0:
                self.mCharge = 0
            # Notify external monitor about drain
            if self.external_monitor:
                self.external_monitor.notify_drain(self.mCharge)
            return True
        return False