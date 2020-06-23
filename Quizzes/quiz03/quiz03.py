# Uses Global Temperature Time Series, avalaible at
# http://data.okfn.org/data/core/global-temp, stored in the file monthly_csv.csv,
# assumed to be stored in the working directory.
# Prompts the user for the source, a year or a range of years, and a month.
# - The source is either GCAG or GISTEMP.
# - The range of years is of the form xxxx -- xxxx (with any number of spaces,
#   possibly none, around --) and both years can be the same,
#   or the first year can be anterior to the second year,
#   or the first year can be posterior to the first year.
# We assume that the input is correct and the data for the requested month
# exist for all years in the requested range.
# Then outputs:
# - The average of the values for that source, for this month, for those years.
# - The list of years (in increasing order) for which the value is larger than that average.
#
# Written by Amritesh Singh and Eric Martin for COMP9021


import sys
import os
import csv
from datetime import datetime

filename = 'assignment01_files/monthly_csv.csv'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

source = input('Enter the source (GCAG or GISTEMP): ')
year_or_range_of_years = input('Enter a year or a range of years in the form XXXX -- XXXX: ')
month = input('Enter a month: ')
average = 0
years_above_average = []

# REPLACE THIS COMMENT WITH YOUR CODE
ctr = 0
total = 0
csv_contents = []

mth = datetime.strptime(month, '%B').month
year_or_range_of_years = tuple(year_or_range_of_years.replace('--', ' ').split())

if len(year_or_range_of_years) is 1:
    year_start = year_end = int(year_or_range_of_years[0])
else:
    if year_or_range_of_years[0] > year_or_range_of_years[1]:
        year_start, year_end = int(year_or_range_of_years[1]), int(year_or_range_of_years[0])
    else:
        year_start, year_end = int(year_or_range_of_years[0]), int(year_or_range_of_years[1])

with open(filename) as file:
    readfile = csv.reader(file, delimiter=',')
    next(readfile)

    for line in readfile:
        csv_contents.append((line[0], line[1], line[2]))

for s, d, m in csv_contents:
    dt = datetime.strptime(d, '%Y-%m-%d')

    if s == source and year_start <= dt.year <= year_end and mth == dt.month:
        total += float(m)
        ctr += 1

average = total / ctr

for s, d, m in csv_contents:
    dt = datetime.strptime(d, '%Y-%m-%d')

    if s == source and year_start <= dt.year <= year_end and mth == dt.month and average < float(m):
        years_above_average.append(dt.year)

years_above_average.sort()

print(f'The average anomaly for {month} in this range of years is: {average:.2f}.')
print('The list of years when the temperature anomaly was above average is:')
print(years_above_average)