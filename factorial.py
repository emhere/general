def factorial(x):
    y=1
    while x != 0:
        y*=x
        x-=1
    else:
        x=y
    return x