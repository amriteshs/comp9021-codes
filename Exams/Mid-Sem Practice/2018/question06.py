
def display(square):
    print('\n'.join(' '.join(f'{x:2d}' for x in row) for row in square))

def check_out_square_and_fix_if_corrupted(square):
    '''
    Call "good square" an n x n matrix with n >= 2 consisting of all numbers
    between 1 and n ** 2.
    Call "corrupted square" a good square exactly one of whose entries has been
    replaced by 0.

    Note: marks can be scored by just checking whether the square is good or corrupted,
    without fixing it in case it is corrupted -- but hard coding won't help.
    
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6  4  8
    It is a good square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 3],\
                                               [6, 10, 8]])
    Here is the square: 
     1  5  7
     2  9  3
     6 10  8
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7],\
                                               [2, 9, 0],\
                                               [6, 4, 8]])
    Here is the square: 
     1  5  7
     2  9  0
     6  4  8
    It is a corrupted square, the good square being:
     1  5  7
     2  9  3
     6  4  8
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [2, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     2  9  0 16
     6  4  8 12
    13 14 15  2
    It is neither a good nor a corrupted square.
    >>> check_out_square_and_fix_if_corrupted([[1, 5, 7, 11],\
                                               [3, 9, 0, 16],\
                                               [6, 4, 8, 12],\
                                               [13, 14, 15, 2]])
    Here is the square: 
     1  5  7 11
     3  9  0 16
     6  4  8 12
    13 14 15  2
    It is a corrupted square, the good square being:
     1  5  7 11
     3  9 10 16
     6  4  8 12
    13 14 15  2
    '''
    n = len(square)
    if n < 2 or any(len(line) != n for line in square):
        return False
    print('Here is the square: ')
    display(square)
    good_square = False
    corrupted_square = False
    # Insert your code here
    squarelist = [j for i in square for j in i]
    
    if len(set(squarelist)) == n ** 2 and all(True if i in range(n ** 2 + 1) else False for i in squarelist):
        if all(i for i in squarelist):
            good_square = True
        else:
            corrupted_square = True
            
            missingval = [i for i in range(1, n ** 2) if i not in squarelist][0]

            for i in range(len(square)):
                for j in range(len(square[i])):
                    if not square[i][j]:
                        square[i][j] = missingval
                        
    if good_square:
        print('It is a good square.')
    else:
        if not corrupted_square:
            print('It is neither a good nor a corrupted square.')
        else:
            print('It is a corrupted square, the good square being:')
            display(square)

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()