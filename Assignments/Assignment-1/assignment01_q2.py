import sys


def flip_condition_1(p, n):
    L = list(p)
    x = n

    L.sort()

    for i in range(len(L)):
        if L[i] < 0 < x:
            L[i] *= -1
            x -= 1
        else:
            break

    if x > 0:
        L.sort()
        L[0] *= ((-1) ** (x % 2))

    return sum(L)


def flip_condition_2(p, n):
    L = list(p)
    x = n
    maxsum = 0

    L.sort()

    for i in L:
        if x:
            maxsum -= i
            x -= 1
        else:
            maxsum += i

    return maxsum


def flip_condition_3(p, n):
    L = list(p)
    x = n
    rangeminsum = 0
    rangesum = 0
    listmaxsum = sum(L)

    for i in range(len(L)):
        if i < x - 1:
            rangesum += L[i]
        elif i is x - 1:
            rangesum += L[i]
            rangeminsum = rangesum
        else:
            rangesum += (L[i] - L[i - x])
            rangeminsum = min(rangeminsum, rangesum)

    return listmaxsum - 2 * rangeminsum


def flip_condition_4(p):
    L = list(p)

    if not L:
        return 0

    maxsum = flip_condition_3(L, 0)

    for switches in range(1, len(L) + 1):
        maxsum = max(maxsum, flip_condition_3(L, switches))

    return maxsum


if __name__ == '__main__':
    try:
        powers = [int(x) for x in input('Please input the heroes\' powers: ').split()]

    except ValueError:
        print('Sorry, these are not valid power values.')
        sys.exit()

    try:
        nb_of_switches = int(input('Please input the number of power flips: '))

        if nb_of_switches < 0 or nb_of_switches > len(powers):
            raise ValueError

    except ValueError:
        print('Sorry, this is not a valid number of power flips.')
        sys.exit()

    f1 = flip_condition_1(powers, nb_of_switches)
    f2 = flip_condition_2(powers, nb_of_switches)
    f3 = flip_condition_3(powers, nb_of_switches)
    f4 = flip_condition_4(powers)

    print(f'Possibly flipping the power of the same hero many times, the greatest achievable power is {f1}.')
    print(f'Flipping the power of the same hero at most once, the greatest achievable power is {f2}.')
    print(f'Flipping the power of nb_of_flips many consecutive heroes, the greatest achievable power is {f3}.')
    print(f'Flipping the power of arbitrarily many consecutive heroes, the greatest achievable power is {f4}.')