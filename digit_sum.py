def digit_sum(n):
    sum_list = []
    while n != 0:
        x=n%10
        sum_list.append(x)
        n = n//10
    else:
        for y in sum_list:
            n+=y
    return n