# -*- coding: utf-8 -*-

def fib(n):
    # print a fibonacci sequences
    result = []
    a, b = 0, 1
    
    while a < n:
        result.append(a)
        a, b = b, a+b
    
    return result
    
print('print fib(100) = ',fib(100))