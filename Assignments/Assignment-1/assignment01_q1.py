import sys


def find_height(d, v):
    h = 0
    ctr = 0
    tmp = 0

    if v == 0:
        return 0

    for i in range(max(d.keys())):
        if i not in d:
            d[i] = 0

    d_new = sorted(d.items())

    for key, val in d_new:
        ctr = val + tmp

        if v <= ctr:
            h = key + v / ctr
            return h
        else:
            v -= ctr

        tmp = ctr

    if v:
        h = d_new[-1][0] + v / ctr + 1

    return h


if __name__ == '__main__':
    try:
        fname = input('Which data file do you want to use? ')

        block_freq = {}

        with open(fname) as file:
            for line in file:
                if not line.isspace():
                    for i in line.split():
                        k = int(i)
                        if k in block_freq:
                            block_freq[k] += 1
                        else:
                            block_freq[k] = 1

        x = int(input('How many decilitres of water do you want to pour down? '))

        if x < 0:
            raise ValueError

    except FileNotFoundError:
        print('Sorry, this file does not exist.')
        sys.exit()

    except ValueError:
        print('Sorry, this input is invalid.')
        sys.exit()

    height = find_height(block_freq, x)

    print(f'The water rises to {height:.2f} centimetres.')