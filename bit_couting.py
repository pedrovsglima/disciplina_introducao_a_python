def countBits(n):
    qnt = [int(i) for i in bin(n)[2:]]
    return sum(qnt)
