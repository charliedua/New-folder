from timeit import default_timer as timer


class Number(object):
    """
    this is the number class
    """
    def __init__(self, value = 0):
        self.value = value
    def CalcCount(self, x, y):
        count = 0
        for i in range(0, self.value):
            if (i % x == 0) and (i % y == 0):
                count += 1;
        return count

import cProfile
import re


num = Number(500000)
start = timer()
num = Number(500000)
cProfile.run('num.CalcCount(5, 3)')
end = timer()
print(end - start)
