import copy


class Position:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def to_nether(self):
        ret = self.copy()
        ret.x = ret.x / 8
        ret.z = ret.z / 8
        return ret

    def to_overworld(self):
        ret = self.copy()
        ret.x = ret.x * 8
        ret.z = ret.z * 8
        return ret

    def distance_to(self, to_pos: 'Position'):
        return (self.x - to_pos.x) ** 2 + (self.y - to_pos.y) ** 2

    def copy(self):
        return copy.copy(self)

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'
