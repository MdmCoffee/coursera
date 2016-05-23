import re as regex

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')

emails = dict()
count = 0

for line in handle:
    line = line.rstrip()
    if regex.search("^From ", line) is None:
        continue
    else:
        addr = line.split()[1]

        if emails.has_key(addr):
            emails[addr] = emails.get(addr) + 1
        else:
            emails[addr] = 1

        count += 1

maxKey = None
maxValue = 0
for key in emails.keys():
    if emails.get(key) > maxValue:
        maxValue = emails.get(key)
        maxKey = key

print maxKey, maxValue