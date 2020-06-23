import sys

def pascal_triangle(n):
    L = [[1] * (i + 1) for i in range(n + 1)]
    
    for i in range(2, len(L)):
        for j in range(1, len(L[i]) - 1):
            L[i][j] = L[i - 1][j] + L[i - 1][j - 1]
            
    return L

def print_triangle(L):
    width = len(str((L[len(L) - 1][(len(L) - 1) // 2])))
    
    for i in range(len(L)):
        print(' ' * width * (len(L) - i - 1), end='')
        
        for j in range(len(L[i])):
            print(f'{L[i][j]:{width}d}', end='')
            
            if j < len(L[i]) - 1:
                print(' ' * width, end='')
        
        print()


if __name__ == '__main__':
    try:
        n = int(input('Enter a nonnegative integer: '))
        
        if n < 0:
            raise ValueError
            
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()  

    L = pascal_triangle(n)
    print_triangle(L)