def decode(x, y):
    line1 = str(x)
    line2 = str(y)
    line3 = str(x * int(line2[1]))
    line4 = str(x * int(line2[0]))
    line5 = str(x * y)
    
    sum1 = int(line1[2]) + int(line2[1]) + int(line3[3]) + int(line5[3])
    sum2 = int(line1[1]) + int(line2[0]) + int(line3[2]) + int(line4[2]) + int(line5[2])
    sum3 = int(line1[0]) + int(line3[1]) + int(line4[1]) + int(line5[1])
    sum4 = int(line3[0]) + int(line4[0]) + int(line5[0])
    
    if sum1 == sum2 == sum3 == sum4:
        stat = True
    else:
        stat = False

    return stat, sum1
    

if __name__ == '__main__':
    for x in range(100, 1000):
        for y in range(10, 100):
            if len(str(x * y)) == 4 and len(str(x * (y % 10))) == 4 and len(str(x * (y // 10))) == 3:
                stat, sumc = decode(x, y)
                
                if stat:
                    print(f'{x} * {y} = {x * y}, all columns adding up to {sumc}.')