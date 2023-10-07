def factorial_loop(n):
    fact = n
    while True:
        print("n=%d, fact=%d" % (n, fact))
        if n <= 1:
            break
        n = n - 1
        fact = fact * n
    return fact


def factorial_rec(n):
    print("n=%d" % n)
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


def factorial_tail_rec(n, fact=1):
    print("n=%d, fact=%d" % (n, fact))
    if n <= 1:
        return fact
    return factorial_tail_rec(n - 1, fact * n)


print(factorial_loop(5))
print(factorial_rec(5))
print(factorial_tail_rec(5))
