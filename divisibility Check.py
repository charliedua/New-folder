import cProfile

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

num = Number(50000000)

cProfile.run('num.CalcCount(3, 5)')
