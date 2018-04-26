from timeit import default_timer as timer



def CalcCount(number, x, y):
    count = 0
    for i in range(0, number):
        if (i % x == 0) and (i % y == 0):
            count += 1;
    return count

import cProfile
import re


CalcCount(500000, 3, 5)
start = timer()
cProfile.run('CalcCount(500000, 3, 5)')

end = timer()
print(end - start)

