def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
        
    return True


if __name__ == '__main__':
    print('The solutions are:')
    print()
    
    L = [x for x in range(10000, 100000) if is_prime(x)]
    
    a = L[0]
    b = L[1]
    c = L[2]
    d = L[3]
    e = L[4]
    f = L[5]
    
    for i in range(6, len(L)):
        if b == a + 2 and c == b + 4 and d == c + 6 and e == d + 8 and f == e + 10:
            print(f'{a} {b} {c} {d} {e} {f}')

        a = L[i - 5]
        b = L[i - 4]
        c = L[i - 3]
        d = L[i - 2]
        e = L[i - 1]
        f = L[i]