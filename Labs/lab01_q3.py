from random import seed, randrange
import sys


try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
    
seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:' , L)
print()

x = [0] * 4

for e in L:
    x[e // 5] += 1
    
for i in range(4):
    if x[i] == 0:
        print('There is no element', end = ' ')
    elif x[i] == 1:
        print('There is 1 element', end = ' ')
    else:
        print(f'There are {x[i]} elements', end = ' ')
    
    if i == 0:
        print(f'between 0 and 4.')
    elif i == 1:
        print(f'between 5 and 9.')
    elif i == 2:
        print(f'between 10 and 14.')
    elif i == 3:
        print(f'between 15 and 19.')