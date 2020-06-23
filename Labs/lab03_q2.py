def is_triple_set(num1, num2, num3):
    s1 = set(str(num1 * num2 * num3))
    
    s2 = set(str(num1)) | set(str(num2)) | set(str(num3))
    
    if s1 == s2 and len(s1) == 6:
        return True
    
    return False


if __name__ == '__main__':    
    for x in range(10, 100):        
        for y in range(x, 100):
            for z in range(y, 100):
                if len(str(x * y * z)) == 6:
                    if is_triple_set(x, y, z):
                        print(f'{x} x {y} x {z} = {x * y * z} is a solution.')
                        