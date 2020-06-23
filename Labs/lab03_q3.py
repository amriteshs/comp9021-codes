def sum_of_squares_set():
    S = [0] * 1000
    
    for a in range(32):
        for b in range(a, 32):
            x = a ** 2 + b ** 2
            
            if x < 100:
                continue
            elif x > 999:
                break

            S[x] = a, b
                
    return S
    
if __name__ == '__main__':    
    L = sum_of_squares_set()

    for i in range(102, len(L)):
        if L[i] and L[i - 1] and L[i - 2]:
            print(f'({i - 2}, {i - 1}, {i}) (equal to ({L[i - 2][0]}^2+{L[i - 2][1]}^2, {L[i - 1][0]}^2+{L[i - 1][1]}^2, {L[i][0]}^2+{L[i][1]}^2)) is a solution.')