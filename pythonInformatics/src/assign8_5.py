import re as regex

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

emails = list()
fh = open(fname, 'r')
count = 0

for line in fh:
    line = line.rstrip()
    if regex.search("^From ", line) is None:
        continue
    else:
        count += 1
        emails.append(line.split()[1])

for addr in emails:
    print(addr)

print "There were", count, "lines in the file with From as the first word"
