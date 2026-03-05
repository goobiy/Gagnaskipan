
def factorial(n: int) -> int:
    assert n >= 0, "No negative numbers"

    if n == 0:
        return 1
    
    return n * factorial(n-1)



def power(base: int, exp: int) -> int:
    assert base >= 0

    if exp == 0:
        return 1
    if base == 0:
        return 0
    if base == 1:
        return 1
    if exp == 1:
        return base
    

    return base * power(base, exp-1)


def weird_multi(a: int,b: int) -> int:

    if a == 0 or b == 0:
        return 0
    
    if a < 0 and b < 0:
        a, b = abs(a), abs(b)
        
    if b < 0:
        return b + weird_multi(a-1,b)

    return a + weird_multi(a, b-1)





def sum_digit(n: int) -> int:

    if n == 0:
        return 0

    sgl = n % 10

    new = n // 10

    return sgl + sum_digit(new)



def fibonacci(n: int) -> int:
    assert n >= 0

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


def foo(d: int) -> int:
    if d <= 0:
        return 1
    cnt = 0
    cnt += foo(d-1)
    cnt += foo(d-1)
    return cnt

print(foo(2))