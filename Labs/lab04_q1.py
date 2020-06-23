import sys

def generate_triangle(n):
    ctr = 0
    
    for i in range(n):
        s = ''
        print(' ' * (n - i - 1), end='')
        
        for j in range(i + 1):
            s += chr((ctr % 26) + ord('A'))
            ctr += 1
            
        print(s[:len(s) - 1] + s[::-1])

if __name__ == '__main__':
    try:
        n = int(input('Enter strictly positive number: '))
        
        if n <= 0:
            raise ValueError
            
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()  

    generate_triangle(n)