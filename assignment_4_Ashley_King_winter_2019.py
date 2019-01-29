'''
Algorithm:

* create a range of years from 1897 to 2012
* for each year in the range
	-- instantiate list of 0's to hold count of each digit in year (digit_count)
	-- instatiate a string that casts the year int into a string
	-- create a list to hold the duplicated digits (new_list)
	* for each digit in the year string
	  -- set number = the digit converted to an int
	  -- increment the corresponding element in digit_count by 1
 	  * loop over range of length of digit_count
	    -- if digit_count at that index > 1. append that element to new_list
	       (this is the list of duplicated numbers)
          * if the length of new_list == 0, no number were duplicated, print year andduplicate status to screen
	    -- else (new_list length > 1)
	       -- create an empty string
	       * for each item in new_list, append spaces and item to new_string
               print the year + the string that shows which numbers are duplicated
'''

year_range = range(1987, 2013)

for year in year_range: #beginning year loop
    digit_count = [0] * 10
    year_string = str(year)
    new_list = []
    for digit in year_string:
        number = int(digit)
        digit_count[number] += 1
    for i in range(len(digit_count)):

        if digit_count[i] > 1:
            new_list.append(i)
    if len(new_list) == 0:
        print(str(year) + " - no duplicates")
    else:
        new_string = ""
        for item in new_list:
            new_string += " " + str(item) + " "
        print(str(year) + " - duplicated number(s):" + new_string)

