class Item:

    def __init__(self, _id, weight, value):
        self.id = _id
        self.weight = weight
        self.value = value

    def to_string(self):
        return '[{}, {}, {}]'.format(self.id, self.weight, self.value)
