def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        print(a)

fib(1000)
