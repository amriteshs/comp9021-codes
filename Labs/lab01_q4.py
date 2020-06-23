from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
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
L = [randint(-50, 50) for _ in range(nb_of_elements)]

print('\nThe list is:', L)

mean_l = sum(L) / len(L)
    
s = 0
for e in L:
    s += ((e - mean_l) ** 2)
    
stddev_l = (s / len(L)) ** 0.5

L.sort()
if not len(L) % 2:
    median_l = (L[len(L) // 2] + L[len(L) // 2 - 1]) / 2
else:
    median_l = L[len(L) // 2]
    
print('\nThe mean is {0:.2f}.'.format(mean_l))
print('The median is {0:.2f}.'.format(median_l))
print('The standard deviation is {0:.2f}.'.format(stddev_l))
print('\nConfirming with functions from the statistics module:')
print('The mean is {0:.2f}.'.format(mean(L)))
print('The median is {0:.2f}.'.format(median(L)))
print('The standard deviation is {0:.2f}.'.format(pstdev(L)))