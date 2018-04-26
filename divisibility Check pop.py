import cProfile

def CalcCount(number, x, y):
    count = 0
    for i in range(0, number):
        if (i % x == 0) and (i % y == 0):
            count += 1;
    return count

CalcCount(50000000, 3, 5)

cProfile.run('CalcCount(500000, 3, 5)')
