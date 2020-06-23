
# ord(c) returns the encoding of character c.
# chr(e) returns the character encoded by e.


def f(width, height):
    '''
    Displays a rectangle by outputting lowercase letters, starting with a,
    in a "snakelike" manner, from left to right, then from right to left,
    then from left to right, then from right to left, wrapping around when z is reached.
    
    >>> f(1, 1)
    a
    >>> f(2, 3)
    ab
    dc
    ef
    >>> f(3, 2)
    abc
    fed
    >>> f(17, 4)
    abcdefghijklmnopq
    hgfedcbazyxwvutsr
    ijklmnopqrstuvwxy
    ponmlkjihgfedcbaz
    '''
    if width <= 0 or height <= 0:
        sys.exit()
    # Insert your code here
    dir = 'L'
    letter = ord('a')
    
    for i in range(height):
        s = ''
        
        if dir is 'L':
            for j in range(width):
                s += chr(letter)
                letter = (letter - 96) % 26 + 97
                
            dir = 'R'
        else:
            for j in range(width):
                s += chr(letter)
                letter = (letter - 96) % 26 + 97
                
            s = s[::-1]
                
            dir = 'L'
            
        print(s)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
