import sys
from random import seed, randrange

try:
    arg_for_seed = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
x = randrange(10 ** 10)
sum_of_digits_in_x = 0
L = [randrange(10 ** 8) for _ in range(10)]
first_digit_greater_than_last = 0
same_first_and_last_digits = 0
last_digit_greater_than_first = 0
distinct_digits = [0] * 9
min_gap = 10
max_gap = -1
first_and_last = set()

# REPLACE THIS COMMENT WITH YOUR CODE
num = x
while num:
    rem, num = num % 10, num // 10
    sum_of_digits_in_x += rem

first_and_last_freq = {}

for l in L:
    first_digit = int(str(l)[0])
    last_digit = l % 10

    if first_digit > last_digit:
        first_digit_greater_than_last += 1
    elif first_digit < last_digit:
        last_digit_greater_than_first += 1
    else:
        same_first_and_last_digits += 1

    min_gap = min(min_gap, abs(first_digit - last_digit))
    max_gap = max(max_gap, abs(first_digit - last_digit))

    unique_digits_in_numbers = set(str(l))
    distinct_digits[len(unique_digits_in_numbers)] += 1

    if (first_digit, last_digit) in first_and_last_freq:
        first_and_last_freq[(first_digit, last_digit)] += 1
    else:
        first_and_last_freq[(first_digit, last_digit)] = 1

max_freq = max(first_and_last_freq.values())

for key, val in first_and_last_freq.items():
    if val == max_freq:
        first_and_last.add(key)

print()
print('x is:', x)
print('L is:', L)
print()
print(f'The sum of all digits in x is equal to {sum_of_digits_in_x}.')
print()
print(f'There are {first_digit_greater_than_last}, {same_first_and_last_digits} '
      f'and {last_digit_greater_than_first} elements in L with a first digit that is\n'
      '  greater than the last digit, equal to the last digit,\n'
      '  and smaller than the last digit, respectively.'
     )
print()
for i in range(1, 9):
    if distinct_digits[i]:
        print(f'The number of members of L with {i} distinct digits is {distinct_digits[i]}.')
print()
print('The minimal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {min_gap}.'
     )
print('The maximal gap (in absolute value) between first and last digits\n'
      f'  of a member of L is {max_gap}.')
print()
print('The number of pairs (f, l) such that f and l are the first and last digits\n'
      f'of members of L is maximal for (f, l) one of {sorted(first_and_last)}.'
     )