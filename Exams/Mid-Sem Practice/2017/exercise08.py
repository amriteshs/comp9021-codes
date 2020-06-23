
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here
    sumset = set()
    
    for i in square:
        s = 0
        
        for j in i:
            s += j
            
        sumset.add(s)
        
    s = [0] * len(square)
    
    for i in range(len(square)):
        for j in range(len(square[i])):
            s[j] += square[i][j]
            
    for i in s:
        sumset.add(i)
        
    s = 0
    
    for i in range(len(square)):
        s += square[i][i]
        
    sumset.add(s)
    
    s = 0
    
    for i in range(len(square)):
        s += square[i][n - i - 1]
    
    sumset.add(s)
    
    if len(sumset) is ((n * 2) + 2):
        return True
        
    return False

# Possibly define other functions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
