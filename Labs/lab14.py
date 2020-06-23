# Uses Heath Nutrition and Population statistics, avalaible at
# http://datacatalog.worldbank.org, stored in the file HNP_Data.csv,
# assumed to be stored in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.


import sys
import os
import csv


filename = 'HNP_Data.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

with open(filename) as file:
    countries_for_max_value_per_year = {}
    max_value = -1
    flag = False
    
    for line in file:
        if not flag:
            flag = True
        else:
            l = line.split(',')
            
            if l[2] == indicator_of_interest:
                for i in range(4, len(l)):
                    try:
                        l[i] = float(l[i])
                        max_value = max(max_value, l[i])
                    except ValueError:
                        continue
                    
    flag = False
    print(file[0][4])
#    for line in file:
#        if not flag:
#            flag = True
#        else:
#            l = line.split(',')
#            
#            if l[2] == indicator_of_interest:
#                for i in range(4, len(l)):
#                    try:
#                        if l[i] == max_value:
#                            
#                    except ValueError:
#                        continue
    
    if max_value == -1:
        max_value = None
#    flag = False
#    
#    for line in file:
#        if not flag:
#            flag = True
#        else:
#            l = line.split(',')
#            
#            for i in l[4:]:
#                if i == max_value:

if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
#    for year in sorted(countries_for_max_value_per_year):
#        print(f'    {year}: {countries_for_max_value_per_year[year]}')