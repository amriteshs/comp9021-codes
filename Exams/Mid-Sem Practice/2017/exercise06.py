import sys            
        
def f(a, b):
    '''
    Finds all numbers i and j with a <= i <= j <= b such that:
    - i + j is even;
    - when read from left to right, the digits in i are strictly increasing
    - when read from left to right, the digits in j are strictly decreasing
    - when read from left to right, the digits in the average of i and j are
      either strictly increasing or strictly decreasing

    Outputs the solutions from smallest i to largest i,
    and for a given i from smallest j to largest j.
    
    >>> f(10, 20)
    12 and 20 with 16 as average
    14 and 20 with 17 as average
    16 and 20 with 18 as average
    18 and 20 with 19 as average
    >>> f(30, 50)
    34 and 40 with 37 as average
    34 and 42 with 38 as average
    34 and 50 with 42 as average
    35 and 41 with 38 as average
    35 and 43 with 39 as average
    36 and 40 with 38 as average
    36 and 42 with 39 as average
    36 and 50 with 43 as average
    37 and 41 with 39 as average
    37 and 43 with 40 as average
    38 and 40 with 39 as average
    38 and 42 with 40 as average
    39 and 41 with 40 as average
    39 and 43 with 41 as average
    46 and 50 with 48 as average
    48 and 50 with 49 as average
    >>> f(400, 700)
    456 and 630 with 543 as average
    457 and 521 with 489 as average
    458 and 520 with 489 as average
    459 and 621 with 540 as average
    468 and 510 with 489 as average
    478 and 542 with 510 as average
    479 and 541 with 510 as average
    489 and 531 with 510 as average
    567 and 653 with 610 as average
    568 and 610 with 589 as average
    568 and 652 with 610 as average
    569 and 651 with 610 as average
    578 and 642 with 610 as average
    579 and 641 with 610 as average
    589 and 631 with 610 as average
    589 and 651 with 620 as average
    589 and 653 with 621 as average
    '''
    if a <= 0 or b < a:
        sys.exit()
    #Insert your code here
    i = a
    
    while i <= b:
        x = str(i)
        order = ['i', 'd']
        order_a = 'x'
        
        if len(x) is 1:
            order_a = order[0]
        else:
            l1 = list(x)
            l1.sort()
            s1 = set(l1)
            tmp1 = ''.join(l1)
            
            if x == tmp1 and len(l1) == len(s1):
                order_a = 'i'
                
        if order_a is order[0]:
            j = i
            
            while j <= b:
                y = str(j)
                order_b = 'x'
                
                if len(y) is 1:
                    order_b = order[1]
                else:
                    l2 = list(y)
                    l2.sort(reverse=True)
                    s2 = set(l2)
                    tmp2 = ''.join(l2)
                    
                    if y == tmp2 and len(l2) == len(s2):
                        order_b = 'd'
                
                if order_b is order[1] and not (i + j) % 2:
                    avg = (i + j) // 2
                    z = str(avg)
                    order_c = 'x'
                    
                    if len(z) is 1:
                        order_c = 'i'
                    else:
                        l3 = list(z)
                        s3 = set(l3)
                        l3.sort()
                        tmp31 = ''.join(l3)
                        l3.sort(reverse=True)
                        tmp32 = ''.join(l3)
                        
                        if len(l3) == len(s3):
                            if z == tmp31:
                                order_c = 'i'
                            elif z == tmp32:
                                order_c = 'd'
                                
                    if order_c in order:
                        print(f'{i} and {j} with {avg} as average')
                    
                j += 1
    
        i += 1

# Possibly define other functions
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
