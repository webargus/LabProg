
import time as t


def fib_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_iter(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    s = 0
    for i in range(2, n+1):
        s = a + b
        a = b
        b = s
    return s


def fib_memo(n, memo=[]):
    if n == 0:
        memo.append(n)
        return 0
    if n == 1:
        memo.append(n)
        return 1
    if n in memo.index():
        return memo[n]

while 1:
    n = int(input("Enter integer > 0 (<0=>exit):"))
    if n < 0:
        break
    init = t.time()
    print(fib_rec(n))
    print("Elapsed time: %d" % (t.time() - init))
    print(fib_iter(n))






