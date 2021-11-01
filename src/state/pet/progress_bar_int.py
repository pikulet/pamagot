class ProgressBarInt:

    def __init__(self, max_value):
        self.value = 0
        self.max_value = max_value

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, value):
        self.value = max_value
        self.value = max(self.value, 0)
        self.value = min(self.value, self.max_value)

    def __add__(self, value):
        self.value += value

    def __sub__(self, value):
        self.value -= value