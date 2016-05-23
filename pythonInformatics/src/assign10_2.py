import re as regex

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name, 'r')

hours = dict()
count = 0

for line in handle:
    line = line.rstrip()
    if regex.search("^From ", line) is None:
        continue
    else:
        hour = line.split()[5].split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

for hour in sorted(hours.keys()):
    print hour, hours.get(hour)
