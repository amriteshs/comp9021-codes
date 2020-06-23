import os.path
import sys
from collections import deque


def distance_from_west(h):
    L = list(h)
    maxdist = 0
    clim = L[0][0]
    flim = L[0][1]

    for x in range(flim, clim):
        d = 0

        for c, f in L:
            if f - 1 < x < c:
                d += 1
            else:
                break

        maxdist = max(maxdist, d)

    return maxdist


def distance_inside_tunnel(h):
    L = deque(h)
    maxdist = 0

    while len(L) > 1:
        maxdist = max(maxdist, distance_from_west(L))
        L.popleft()

    return maxdist


if __name__ == '__main__':
    try:
        fname = input('Please enter the name of the file you want to get data from: ')

        if os.path.isfile(fname):
            h_ceil = []
            h_floor = []
            heights = []

            with open(fname) as file:
                flag = False

                for line in file:
                    if not line.isspace():
                        ctr = 0

                        for i in line.split():
                            k = int(i)
                            ctr += 1

                            if flag:
                                h_floor.append(k)
                            else:
                                h_ceil.append(k)

                        if ctr < 2:
                            raise ValueError

                        if not flag:
                            flag = True

            if len(h_ceil) is not len(h_floor):
                raise ValueError

            for i, j in zip(h_ceil, h_floor):
                if i <= j:
                    raise ValueError
                else:
                    heights.append((i, j))
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        print('Sorry, there is no such file.')
        sys.exit()

    except ValueError:
        print('Sorry, input file does not store valid data.')
        sys.exit()

    print(f'From the west, one can see into the tunnel over a distance of {distance_from_west(heights)}.')
    print(f'Inside the tunnel, one can see into the tunnel over a maximum distance of {distance_inside_tunnel(heights)}.')