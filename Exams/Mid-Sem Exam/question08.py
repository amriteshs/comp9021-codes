'''
Will be tested with letters a string of DISTINCT UPPERCASE letters only.
'''
from itertools import permutations


def f(letters):
    '''
    >>> f('ABCDEFGH')
    There is no solution
    >>> f('GRIHWSNYP')
    The pairs of words using all (distinct) letters in "GRIHWSNYP" are:
    ('SPRING', 'WHY')
    >>> f('ONESIX')
    The pairs of words using all (distinct) letters in "ONESIX" are:
    ('ION', 'SEX')
    ('ONE', 'SIX')
    >>> f('UTAROFSMN')
    The pairs of words using all (distinct) letters in "UTAROFSMN" are:
    ('AFT', 'MOURNS')
    ('ANT', 'FORUMS')
    ('ANTS', 'FORUM')
    ('ARM', 'FOUNTS')
    ('ARMS', 'FOUNT')
    ('AUNT', 'FORMS')
    ('AUNTS', 'FORM')
    ('AUNTS', 'FROM')
    ('FAN', 'TUMORS')
    ('FANS', 'TUMOR')
    ('FAR', 'MOUNTS')
    ('FARM', 'SNOUT')
    ('FARMS', 'UNTO')
    ('FAST', 'MOURN')
    ('FAT', 'MOURNS')
    ('FATS', 'MOURN')
    ('FAUN', 'STORM')
    ('FAUN', 'STROM')
    ('FAUST', 'MORN')
    ('FAUST', 'NORM')
    ('FOAM', 'TURNS')
    ('FOAMS', 'RUNT')
    ('FOAMS', 'TURN')
    ('FORMAT', 'SUN')
    ('FORUM', 'STAN')
    ('FORUMS', 'NAT')
    ('FORUMS', 'TAN')
    ('FOUNT', 'MARS')
    ('FOUNT', 'RAMS')
    ('FOUNTS', 'RAM')
    ('FUR', 'MATSON')
    ('MASON', 'TURF')
    ('MOANS', 'TURF')
    '''
    dictionary = 'dictionary.txt'
    solutions = []
    # Insert your code here
    L = []
    words = []

    for i in letters:
        L.append(i)

    with open(dictionary) as file:
        for line in file:
            if not line.isspace():
                X = set([i for i in line if i not in ('\n', ' ', '')])
                m = line.rstrip('\n')
                if len(X) == len(line) - 1 and len(X | set(L)) == len(set(L)):
                    words.append(m)

    visited = []

    for i in words:
        if i not in visited:
            visited.append(i)
        else:
            continue

        rem = ''.join([j for j in L if j not in i])

        for k in permutations(rem):
            if ''.join(k) in words and ''.join(k) not in visited:
                solutions.append((i, ''.join(k)))
                visited.append(''.join(k))

    for i in range(len(solutions)):
        x = [solutions[i][0], solutions[i][1]]
        x.sort()
        solutions[i] = solutions[i][0], solutions[i][1]

    if not solutions:
        print('There is no solution')
    else:
        print(f'The pairs of words using all (distinct) letters in "{letters}" are:')
        for solution in solutions:
            print(solution)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
