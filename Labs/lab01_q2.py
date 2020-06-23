from random import seed, randint
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
L = [randint(0, 99) for _ in range(nb_of_elements)]

print('\nThe list is:', L)

max_element = 0
min_element = 99

for e in L:
    if e > max_element:
        max_element = e
    
    if e < min_element:
        min_element = e

print('\nThe maximum difference between largest and smallest values in this list is:', max_element - min_element)
print('Confirming with builtin operations:', max(L) - min(L))