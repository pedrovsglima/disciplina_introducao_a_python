def high_and_low(numbers):
    num = [int(x) for x in numbers.split()]
    return "{} {}".format(max(num), min(num))
