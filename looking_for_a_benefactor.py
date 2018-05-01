import math

def new_avg(arr, newavg):
    x = (newavg * (len(arr)+1)) - sum(arr)
    if x > 0:
        return math.ceil(x)
    else:
        raise ValueError('-1')
