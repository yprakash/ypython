import functools


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    print('Generating fibonacci for', n)
    return fibonacci(n - 1) + fibonacci(n - 2)


@functools.lru_cache(maxsize=128)
def factorial(n):
    if n <= 1:
        return 1
    print('Generating factorial for', n)
    return n * factorial(n - 1)
