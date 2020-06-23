'''
Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv
from datetime import datetime

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    # Insert your code here
    csv_contents = []
    
    with open('cpiai.csv') as file:
        readfile = csv.reader(file, delimiter=',')
        next(readfile)
        
        for line in readfile:
            k = line[0].split('-')
            csv_contents.append((int(k[0]), months[int(k[1]) - 1], float(line[2])))
    
    max_inflation = max([i[2] for i in csv_contents if i[0] == year])
    months_list = ', '.join([i[1] for i in csv_contents if i[0] == year and i[2] == max_inflation])

    print(f'In {year}, maximum inflation was: {max_inflation}')
    print(f'It was achieved in the following months: {months_list}')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
