fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    lst += line.rstrip().split()

lst.sort()
print(lst)
