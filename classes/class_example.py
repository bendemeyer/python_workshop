class Incrementor(object):
    class_attribute = "Set at class level"
    shared_attribute = "Set at class level"

    def __init__(self):
        self.instance_attribute = "Set at instance level"
        self.shared_attribute = "Set at instance level"
        self._value = 0

    def _add(self, number):
        self._value += number

    def increment(self):
        self._add(1)

    @classmethod
    def incrementor_factory(cls, value):
        instance = cls()
        instance._value = value
        return instance

    @staticmethod
    def instance_is_value(incrementor, value):
        return incrementor._value == value