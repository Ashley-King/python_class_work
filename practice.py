x = []
y = []

for i in range(5,  60,  10) :
     fi = i / 10.0
     x.append(fi)
     y.append(fi)

d = (i/10.0 for i in range(5,60, 10))
e = (i/10.0 for i in range(5,60, 10))

print('\t   '),
for i in range(5, 60, 10):
    fi = i/10.0
    print("\t\t" + str(fi)),
for i in range(5, 60, 10):
    fi = i/10.0
    print '\n','{:02}'.format(fi),' ',
    for j in range(5, 60, 10):
        fj = j/10.0
        print '\t\t{:02}'.format(fi*fj),