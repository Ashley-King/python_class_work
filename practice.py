x = []
y = []

for i in range(5,  60,  10) :
     fi = i / 10.0
     x.append(fi)
     y.append(fi)

# for index in range(len(x)):
#     print x[index]
for index in range(len(x)):
    row_out = "{0:10.2f}".format(x[index])
    print(row_out),
print'\n'
for index in range(len(y)):
    print('{:0.2f}'.format(y[index]))
    for jindex in range(len(x)):
        print('{:0.2f}'.format(y[index] + x[jindex])),

# d = (i/10.0 for i in range(5,60, 10))
# e = (i/10.0 for i in range(5,60, 10))
#
# print('\t   '),
# for i in range(5, 60, 10):
#     fi = i/10.0
#     print("\t\t" + str(fi)),
# for i in range(5, 60, 10):
#     fi = i/10.0
#     print '\n','{:02}'.format(fi),' ',
#     for j in range(5, 60, 10):
#         fj = j/10.0
#         print '\t\t{:02}'.format(fi*fj),

        # row_out = "item #{} is {:15.2f}".format(index, various_nums[index])