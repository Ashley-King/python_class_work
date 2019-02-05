"""
    Assignment: 4 - Sponge Bod's Year Conjecture & Non-Integral
                    Multiplication Table
    Author: Ashley King
    Date: 2019-01-31
    Description: Loops & Formatting
"""

"""
Part 1 Algorithm:

1. create a range of years from 1897 to 2012
2. for each year in the range
-- instantiate list of 0's to hold count of each digit in year (digit_count)
-- instantiate a string that casts the year int into a string
-- create a list to hold the duplicated digits (new_list)
3. for each digit in the year string
-- set number = the digit converted to an int
-- increment the corresponding element in digit_count by 1
4. loop over range of length of digit_count
-- if digit_count at that index > 1, append that element to new_list
   (this is the list of duplicated numbers)
5. if the length of new_list == 0, no number were duplicated,
   print year andduplicate status to screen
-- else (new_list length > 1)
-- create an empty string
6. for each item in new_list, append spaces and item to new_string
   print the year + the string that shows which numbers are duplicated
"""

print("----------------- Duplicate Digits -----------------")

year_range = range(1987, 2013)

for year in year_range:
    # create list to hold digit count
    digit_count = [0] * 10
    year_string = str(year)
    # create list to hold duplicate digits
    new_list = []
    for digit in year_string:
        number = int(digit)
        # increment digit_count if digit exists at that index
        digit_count[number] += 1
    for i in range(len(digit_count)):
        if digit_count[i] > 1:
            # if there's more than one of a particular digit, add it to the list
            new_list.append(i)
    # if there are no duplicates, say so
    if len(new_list) == 0:
        print(str(year) + " - no duplicates")
    # else, print the numbers that were duplicated
    else:
        new_string = ""
        for item in new_list:
            new_string += " " + str(item) + " "
        print(str(year) + " - duplicated number(s):" + new_string)
print()

'''----------------- OUTPUT PART 1 -----------------

----------------- Duplicate Digits -----------------
1987 - no duplicates
1988 - duplicated number(s): 8 
1989 - duplicated number(s): 9 
1990 - duplicated number(s): 9 
1991 - duplicated number(s): 1  9 
1992 - duplicated number(s): 9 
1993 - duplicated number(s): 9 
1994 - duplicated number(s): 9 
1995 - duplicated number(s): 9 
1996 - duplicated number(s): 9 
1997 - duplicated number(s): 9 
1998 - duplicated number(s): 9 
1999 - duplicated number(s): 9 
2000 - duplicated number(s): 0 
2001 - duplicated number(s): 0 
2002 - duplicated number(s): 0  2 
2003 - duplicated number(s): 0 
2004 - duplicated number(s): 0 
2005 - duplicated number(s): 0 
2006 - duplicated number(s): 0 
2007 - duplicated number(s): 0 
2008 - duplicated number(s): 0 
2009 - duplicated number(s): 0 
2010 - duplicated number(s): 0 
2011 - duplicated number(s): 1 
2012 - duplicated number(s): 2 
----------------- END OUTPUT PART 1 -----------------'''


"""
Part 2 Algorithm:

    1. instantiate constants to hold list of numbers for headings
    2. create lists using range of numbers & format numbers as floats
    3. loop through and print horizontal headings
    4. loop through vertical row list, print one vertical heading
       and then loop through horizontal row and print multiplication results
       in same row; repeat for entire list
"""

print("----------------- Multiplication Table -----------------")

horiz_row = []
vert_row = []
# create lists
for num in range(5,  60,  10) :
     new_num = num / 10.0
     horiz_row.append(new_num)
     vert_row.append(new_num)
print()
# print horizontal headings
for item in horiz_row:
    print("\t{:.2f}".format(item), end = ' ')
print()
# print vertical row labels, then loop through
# horizontal row, multiply and print results
for item in vert_row:
    print('{:.2f}'.format(item), end=' ')
    for element in horiz_row:
        print('  {:5.2f}'.format(item * element), end=' ')
    print()


'''----------------- OUTPUT PART 2 -----------------

----------------- Multiplication Table -----------------

        0.50    1.50    2.50    3.50    4.50    5.50 
0.50    0.25    0.75    1.25    1.75    2.25    2.75 
1.50    0.75    2.25    3.75    5.25    6.75    8.25 
2.50    1.25    3.75    6.25    8.75   11.25   13.75 
3.50    1.75    5.25    8.75   12.25   15.75   19.25 
4.50    2.25    6.75   11.25   15.75   20.25   24.75 
5.50    2.75    8.25   13.75   19.25   24.75   30.25 
----------------- END OUTPUT PART 2 -----------------'''