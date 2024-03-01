def sum_even_fibonacci(limit):
    sum_even = 0
    fib1, fib2 = 1, 2

    while fib2 <= limit:
        if fib2 % 2== 0:
            sum_even += fib2
        
        # generate the next fibonacci number
        fib1, fib2 = fib2, fib1 + fib2
    
    return sum_even

result = sum_even_fibonacci(3000000)
print(result)