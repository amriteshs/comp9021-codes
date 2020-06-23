

def f(word):
    '''
    Recall that if c is an ascii character then ord(c) returns its ascii code.
    Will be tested on nonempty strings of lowercase letters only.

    >>> f('x')
    The longest substring of consecutive letters has a length of 1.
    The leftmost such substring is x.
    >>> f('xy')
    The longest substring of consecutive letters has a length of 2.
    The leftmost such substring is xy.
    >>> f('ababcuvwaba')
    The longest substring of consecutive letters has a length of 3.
    The leftmost such substring is abc.
    >>> f('abbcedffghiefghiaaabbcdefgg')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is bcdefg.
    >>> f('abcabccdefcdefghacdef')
    The longest substring of consecutive letters has a length of 6.
    The leftmost such substring is cdefgh.
    '''
    desired_length = 0
    desired_substring = ''
    # Insert your code here
    
    if len(word) is 1:
        desired_length = len(word)
        desired_substring = word
    else:
        L = []
        X = [word[0]]
        
        for i in range(1, len(word)):
            if ord(word[i]) == ord(word[i - 1]) + 1:
                X.append(word[i])
            else:
                if X:
                    L.append(X)
                    
                X = [word[i]]
        
        if X:
            L.append(X)
        
        desired_length = max([len(i) for i in L])
        desired_substring = [''.join(i) for i in L if len(i) == desired_length][0]
        
    print(f'The longest substring of consecutive letters has a length of {desired_length}.')
    print(f'The leftmost such substring is {desired_substring}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
