def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def summation (n):
    if n == 0:
        return 1
    return n + summation(n-1)
    
    
def exponent (base, exp):
    if exp == 0:
        return 1
    if exp == 0:
        return 1
    else:
        return base * exponent(base, exp - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

def product_digits(n): 
        if n < 10:
            return n
        return (n % 10) * product_digits(n // 10)

def multiply(a, b):
        if b < 0:
            return -multiply(a, -b)
        if b == 0:
            return 0
        return a + multiply(a, b - 1)
    
def reverse_number(n, reversed_num = 0):
    if n == 0:
        return reversed_num
    last_digit = n % 10
    new_reversed = (reversed_num * 10) + last_digit
    return reverse_number(n // 10, new_reversed)

    

def main ():
    print(factorial(5))
    print(summation(5))
    print(exponent(5,3))
    print(fibonacci (5))
    print(sum_digits(555))
    print(product_digits(555))
    print(multiply(5,5))
    print(reverse_number(654321))
    
main()