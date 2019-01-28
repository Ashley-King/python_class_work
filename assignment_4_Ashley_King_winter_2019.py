year_range = [1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997,
         1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008,
         2009, 2010, 2011, 2012]

for year in year_range:
    new_list = []
    year_string = str(year)
    digi_count = [0] * 10
    for element in year_string:
        digit = int(element)
        print digit
        digi_count[digit] += 1
        for item in digi_count:
            if item > 0:
                new_list.append(item)
                print("new list: " + str(len(new_list)))
    if len(new_list) == 0:
        print(year_string + ' - no dulpicates')
    else:
        print(year_string + ' - duplicates are:')