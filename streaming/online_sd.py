from math import sqrt


def online_sd():
    mean = int(input("Enter first number: "))
    powerSum = 0
    n = 1
    print('x:', mean, 'count:', n, 'mean:', mean, 'sd:', powerSum)

    while True:
        x = int(input("Enter next number: "))
        n += 1
        newMean = mean + (x - mean) / n
        powerSum += (x - mean) * (x - newMean)
        mean = newMean
        yield x, n, mean, sqrt(powerSum / (n-1))


nums = online_sd()
while True:
    x, n, mean, sd = next(nums)
    print('x:', x, 'count:', n, 'mean:', mean, 'sd:', sd)
