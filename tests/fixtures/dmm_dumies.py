import random


class DummyDMMConstant:
    @staticmethod
    def mocked_get_vh1():
        return 1.0
    @staticmethod
    def mocked_get_vh2():
        return 1.02


class DummyDMMThresholdExceeded:
    @staticmethod
    def mocked_get_vh1():
        return 1.8
    @staticmethod
    def mocked_get_vh2():
        return 0.0


class DummyDMMRandomClose:
    def __init__(self, seed: int = 123):
        self.rng = random.Random(seed)

    def mocked_get_vh1(self):
        return self.rng.uniform(0.9, 1.1)

    def mocked_get_vh2(self):
        base = self.rng.uniform(0.9, 1.1)
        return base + self.rng.uniform(-0.01, 0.01)


class DummyDMMRandomCorrelated:
    def __init__(self, seed: int = 321, window: float = 0.03):
        self.rng = random.Random(seed)
        self._last = None
        self.window = window

    def mocked_get_vh1(self):
        v = self.rng.uniform(0.8, 1.2)
        self._last = v
        return v

    def mocked_get_vh2(self):
        base = self._last if self._last is not None else self.rng.uniform(0.8, 1.2)
        return base + self.rng.uniform(-self.window, self.window)
