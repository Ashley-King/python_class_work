# x = []
# y = []
#
# for i in range(5,  60,  10) :
#      fi = i / 10.0
#      x.append(fi)
#      y.append(fi)
#
# # for index in range(len(x)):
# #     print x[index]
# for index in range(len(x)):
#     row_out = "{0:10.2f}".format(x[index])
#     print(row_out),
# print'\n'
# for index in range(len(y)):
#     print('{:0.2f}'.format(y[index]))
#     for jindex in range(len(x)):
#         print('{:0.2f}'.format(y[index] + x[jindex]))

# horiz_row = (i/10.0 for i in range(5,60, 10))
# vert_row = (i/10.0 for i in range(5,60, 10))
# #
# # print('\t   '),
# # for el in horiz_row:
# #     print("\t" + str(el), end=" ")
# #
# # for item in vert_row:
# #     print('\n{:02}'.format(item), end=" ")
# for j in horiz_row:
#     print('this')

#     print ('\t{:02}'.format(i*j)),

# header = []
# for i in range(1, 10):
#     header.append('{0:>2}'.format(i))
#
# rows = []
# for i in range(1, 10):
#    row = []
#    for q in range(1, 10):
#      result = '{0:>2}\t'.format(i*q)
#      row.append(result)
#    rows.append(row)
#
# print('\t{0:>2}'.format('\t'.join(header)))
# for idx, row in enumerate(rows):
#    print('{0:>2}\t{1}'.format(idx+1, ''.join(row)))

# row_out = "item #{} is {:15.2f}".format(index, various_nums[index])


# instantiate constants to hold array of numbers for headings
# loop through and assign headings

# print tab and loop statement to print headings
# print statement to go to next line
# outer loop process one complete horiz row in each pass
# separate print statement before inner loop to print row label on left
# inner loop process individual components of single row & format/output


x = []
y = []

for i in range(5,  60,  10) :
     fi = i / 10.0
     x.append(fi)
     y.append(fi)
print('\t   ', end=' ')
for h in x:
    print("\t" + str(h), end = " ")
print()
for h in x:
    print(h, end=' ')
    for v in y:
        print('\t{0:.2f}'.format(v*h), end=" ")
    print()




