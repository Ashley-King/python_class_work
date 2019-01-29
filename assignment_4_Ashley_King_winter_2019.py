year_range = range(1987, 2013)

for year in year_range: #beginning year loop
    digit_count = [0] * 10
    year_string = str(year)
    for digit in year_string:
        number = int(digit)
        digit_count[number] += 1
    for digi in digit_count:
