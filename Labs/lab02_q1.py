import sys
from math import factorial

def method1(f):
    num = factorial(n)
    
    ctr = 0
    while num:
        if not num % 10:
            ctr += 1
        else:
            break
        
        num //= 10
        
    return ctr

    
def method2(f):
    num = str(factorial(n))
    
    ctr = 0
    for i in range(len(num) - 1, -1, -1):
        if not int(num[i]):
            ctr += 1
        else:
            break
    
    return ctr
    
    
def method3(f):
    num = n
    ctr_2 = 0
    ctr_5 = 0
    
    for i in range(2, num + 1):
        j = i
        while j:
            if not j % 2:
                ctr_2 += 1
            else:
                break
            
            j //= 2
            
        j = i
        while j:
            if not j % 5:
                ctr_5 += 1
            else:
                break
            
            j //= 5
            
        
    return min(ctr_2, ctr_5)


if __name__ == '__main__':
    try:
        n = int(input('Input a nonnegative integer: '))
        
        if n < 0:
            raise ValueError
            
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()  

    print(f'Computing the number of trailing 0s in {n}! by dividing by 10 for long enough: {method1(n)}')
    print(f'Computing the number of trailing 0s in {n}! by converting it into a string: {method2(n)}')
    print(f'Computing the number of trailing 0s in {n}! the smart way: {method3(n)}')