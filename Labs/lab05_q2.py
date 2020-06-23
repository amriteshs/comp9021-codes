import sys


def longest_sequence(seq):
    
    
    return 0

if __name__ == '__main__':
    try:
        w = input('Please input a string of lowercase letters: ')
        
    except ValueError:
        print('Incorrect input, giving up.')
        sys.exit()
        
    print(f'The solution is: {longest_sequence(w)}')