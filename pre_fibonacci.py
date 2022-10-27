def fib(n):
    fib_numbers = []
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        fib_numbers.append(a)
        #print(a)
    print(fib_numbers)

fib(20000)


