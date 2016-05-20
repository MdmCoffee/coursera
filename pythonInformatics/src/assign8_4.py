fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    tempList = line.rstrip().split()
    for word in tempList:
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
