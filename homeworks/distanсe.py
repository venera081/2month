class Distance:
    units = {
        "мм": 0.001,
        "см": 0.01,
        "м": 1,
        "км": 1000
    }

    def __init__(self, value, unit):
        if unit not in Distance.units:
            raise ValueError("Такой единицы измерения нет")
        self.value = value
        self.unit = unit

    def to_meters(self):
        return self.value * Distance.units[self.unit]

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        if self.unit != other.unit:
            to_meter = self.to_meters() + other.to_meters()
            result = to_meter /  Distance.units[self.unit]
            return Distance(round(result, 4), self.unit)
        else:
            return Distance(self.value + other.value, self.units)

    def __sub__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        to_meter = self.to_meters() - other.to_meters()
        if to_meter < 0:
            raise ValueError("Результат не может быть отрицательным")
        result = to_meter /  Distance.units[self.unit]
        return Distance(round(result, 4), self.unit)

    def __lt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() < other.to_meters()

    def __le__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() >= other.to_meters()




