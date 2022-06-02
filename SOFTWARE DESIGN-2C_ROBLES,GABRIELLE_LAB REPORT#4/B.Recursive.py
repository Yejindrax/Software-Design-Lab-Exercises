def product(m, n):
    # if m is less than n swap
    # the numbers
    if m < n:
        return product(n, m)

    # iteratively calculate n
    # times sum of m
    elif n != 0:
        return (m + product(m, n - 1))

    # if any of the two numbers is
    # zero return zero
    else:
        return 0


# Driver code
m = 5
n = 2
print(product(m, n))