from timeit import default_timer as timer

start = timer()

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

end = timer()
print(end - start)



#load time = 0.00003026777867325021

start = timer()

Num = Number(10000)
Num.CalcCount(3, 5)

end = timer()
print(end - start)
