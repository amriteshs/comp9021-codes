import sys

def is_perfect(num):
    P = []
    
    for i in range(1, num // 2 + 1):
        if not num % i:
            P.append(i)

    if num == sum(P):
        return True
    
    return False


if __name__ == '__main__':
    try:
        n = int(input('Input an integer: '))
            
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()  

    for i in range(2, n + 1):
        if is_perfect(i):
            print(f'{i} is a perfect number.')