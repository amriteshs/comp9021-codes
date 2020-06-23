# Prompts the user for a nonnegative integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived nonnegative number that codes the set of running sums
# of the members of S when those are listed in increasing order.
#
# Computes the ordered list of members of a coded set.
#
# Written by Amritesh Singh and Eric Martin for COMP9021


import sys

try:
    encoded_set = int(input('Input a nonnegative integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


def display(L):
    print('{', end='')
    print(', '.join(str(e) for e in L), end='')
    print('}')


def decode(encoded_set):
    decoded_set = []
    encoded_set_binary = bin(encoded_set)[2:][::-1]

    for i in range(len(encoded_set_binary) - 1, -1, -1):
        b = int(encoded_set_binary[i])

        if b:
            if i % 2:
                decoded_set.append(int(-0.5 * (i + 1)))
            else:
                decoded_set.append(int(i / 2))

    decoded_set.sort()

    return decoded_set


def code_derived_set(encoded_set):
    running_sum = 0
    encoding = 0
    derived_set = set()
    decoded_set = decode(encoded_set)

    for i in decoded_set:
        running_sum += i
        derived_set.add(running_sum)

    for i in derived_set:
        if i < 0:
            encoding += (2 ** ((-2 * i) - 1))
        else:
            encoding += (2 ** (i * 2))

    return encoding


print('The encoded set is: ', end='')
display(decode(encoded_set))
code_of_derived_set = code_derived_set(encoded_set)
print('The derived set is encoded as:', code_of_derived_set)
print('It is: ', end='')
display(decode(code_of_derived_set))