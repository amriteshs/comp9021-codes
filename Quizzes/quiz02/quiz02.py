# Written by Amritesh Singh and Eric Martin for COMP9021


import sys
from random import seed, randint
from math import gcd

try:
    arg_for_seed, length, max_value = input('Enter three strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 1 or length < 1 or max_value < 1:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(1, max_value) for _ in range(length)]
print('Here is L:')
print(L)
print()

size_of_simplest_fraction = None
simplest_fractions = []
size_of_most_complex_fraction = None
most_complex_fractions = []
multiplicity_of_largest_prime_factor = 0
largest_prime_factors = []

# REPLACE THIS COMMENT WITH YOUR CODE
fractions = {}

for i in L:
    for j in L:
        if i / j <= 1:
            memx = int(i / gcd(i, j))
            memy = int(j / gcd(i, j))

            if (memx, memy) not in fractions:
                fractions[(memx, memy)] = len(str(memx)) + len(str(memy))

size_of_simplest_fraction = min(fractions.values())
size_of_most_complex_fraction = max(fractions.values())

fractions = sorted(fractions.items(), key=lambda k: (k[0][0] / k[0][1]))

for key, value in fractions:
    if value == size_of_simplest_fraction:
        simplest_fractions.append(key)

    if value == size_of_most_complex_fraction:
        most_complex_fractions.insert(0, key)

most_complex_fractions_denominators = {j for (i, j) in most_complex_fractions}
prime_factors = {}

for item in most_complex_fractions_denominators:
    num = item
    itr = 2
    ctr = 0

    while True:
        if itr <= num:
            if not num % itr:
                ctr += 1

                if itr in prime_factors and ctr > prime_factors[itr]:
                    prime_factors[itr] = ctr
                elif itr not in prime_factors:
                    prime_factors[itr] = 1

                num //= itr
            else:
                ctr = 0
                itr += 1
        else:
            break

if prime_factors:
    multiplicity_of_largest_prime_factor = max(prime_factors.values())

    largest_prime_factors = [key for key, val in sorted(prime_factors.items()) if val == multiplicity_of_largest_prime_factor]

print('The size of the simplest fraction <= 1 built from members of L is:',
      size_of_simplest_fraction
      )
print('From smallest to largest, those simplest fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in simplest_fractions))
print('The size of the most complex fraction <= 1 built from members of L is:',
      size_of_most_complex_fraction
      )
print('From largest to smallest, those most complex fractions are:')
print('\n'.join(f'    {x}/{y}' for (x, y) in most_complex_fractions))
print("The highest multiplicity of prime factors of the latter's denominators is:",
      multiplicity_of_largest_prime_factor
      )
print('These prime factors of highest multiplicity are, from smallest to largest:')
print('   ', largest_prime_factors)