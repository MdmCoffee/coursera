# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname, 'r')

theNum = None
numLines = 0
theSum = 0.0
theAvg = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        line.strip()
        _, num = line.split(':')
        numLines += 1
        theSum += float(num.rstrip())
        theAvg = theSum / numLines

print "Average spam confidence:", theAvg
