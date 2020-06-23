def is_magic_square(square):
    sumset = set()
    
    for i in range(len(square)):
        s = 0
        
        for j in range(len(square[i])):
            s += square[i][j]
            
        sumset.add(s)
        
    s = [0] * len(square)
    
    for i in range(len(square)):
        for j in range(len(square[i])):
            s[j] += square[i][j]
            
    sumset |= set(s)
    
    s = 0
    for i in range(len(square)):
        s += square[i][i]
    
    sumset.add(s)
    
    s = 0
    for i in range(len(square)):
        s += square[i][len(square) - i - 1]
        
    sumset.add(s)
    
    if len(sumset) == 1:
        return True
    
    return False
    
            
def print_square(square):
    for i in range(len(square)):
        for j in range(len(square[i])):
            if j == len(square[i]) - 1:
                print(square[i][j])
            else:
                print(square[i][j], end=' ')