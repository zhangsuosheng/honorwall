#!/home/jingbo/bin/anaconda3/bin/python
import numpy as np
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class JiuGong:
    def __init__(self, stat, blank_position):
        self.stat = stat
        self.blank_position = blank_position

    def __str__(self):
        return '''
        {} {} {}
        {} {} {}
        {} {} {}'''.format(*self.stat.flatten().tolist())

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.rank < other.rank

    def __eq__(self, other):
        return np.array_equal(self.stat, other.stat)

    def __hash__(self):
        return hash(tuple(map(tuple, self.stat)))

    def movable(self, direction: Direction):
        row, column = self.blank_position
        if direction == Direction.UP:
            return row != 0
        if direction == Direction.DOWN:
            return row != 2
        if direction == Direction.LEFT:
            return column != 0
        if direction == Direction.RIGHT:
            return column != 2

    def move(self, direction: Direction):
        x_old, y_old = self.blank_position
        x, y = self.blank_position
        stat = self.stat.copy()
        if direction == Direction.UP:
            x -= 1
        if direction == Direction.DOWN:
            x += 1
        if direction == Direction.LEFT:
            y -= 1
        if direction == Direction.RIGHT:
            y += 1
        stat[x, y], stat[x_old, y_old] = stat[x_old, y_old], stat[x, y]
        return JiuGong(stat, (x, y))

    def count_difference(self, other):
        non_equal_indices = np.nonzero(self.stat - other.stat)
        return len(non_equal_indices[0])
