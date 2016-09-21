def digit_sum(n):
    y = 0
    while n != 0:
        x = n % 10
        y += x
        n //= 10
    n += y
    return n
