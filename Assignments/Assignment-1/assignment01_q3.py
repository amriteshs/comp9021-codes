import os.path
import sys

from collections import defaultdict


def check_perfect_ride(p):
    L = list(p)
    diff = L[1] - L[0]

    for i in range(1, len(L) - 1):
        if diff is not L[i + 1] - L[i]:
            return False

    return True


def longest_good_ride(p):
    L = list(p)
    maxlen = 0
    currlen = 1
    diff = L[1] - L[0]

    for i in range(1, len(L) - 1):
        if diff is L[i + 1] - L[i]:
            currlen += 1
        else:
            diff = L[i + 1] - L[i]
            maxlen = max(currlen, maxlen)
            currlen = 1

    return maxlen


def minimal_pillars_to_remove(p):
    L = list(p)
    slopesval = defaultdict(int)
    slopeslist = defaultdict(list)

    for i in range(1, len(L)):
        for j in range(i):
            diff = L[i] - L[j]
            slopeslist[i].append(diff)

            if diff not in slopesval:
                slopesval[diff] = 2
            elif diff in slopeslist[j]:
                slopesval[diff] += 1

    return len(L) - max(slopesval.values())


if __name__ == '__main__':
    try:
        fname = input('Please enter the name of the file you want to get data from: ')

        if os.path.isfile(fname):
            pillar_heights = []

            with open(fname) as file:
                ctr = 0
                j = 0

                for line in file:
                    if not line.isspace():
                        for i in line.split():
                            k = int(i)
                            ctr += 1

                            if k > j:
                                j = k
                            else:
                                raise ValueError

                            if k <= 0:
                                raise ValueError

                            pillar_heights.append(k)

                if ctr < 2:
                    raise ValueError
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        print('Sorry, there is no such file.')
        sys.exit()

    except ValueError:
        print('Sorry, input file does not store valid data.')
        sys.exit()

    if check_perfect_ride(pillar_heights):
        print(f'The ride is perfect!')
        print(f'The longest good ride has a length of: {len(pillar_heights) - 1}')
        print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: 0.')
    else:
        print(f'The ride could be better...')
        print(f'The longest good ride has a length of: {longest_good_ride(pillar_heights)}')
        print(f'The minimal number of pillars to remove to build a perfect ride from the rest is: {minimal_pillars_to_remove(pillar_heights)}')
