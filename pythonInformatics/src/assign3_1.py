
    hrs = raw_input("Enter Hours:")
h = float(hrs)
rate = float(raw_input("Enter Rate:"))

if h <= 40:
    print h * rate
else:
    overtime = h - 40
    print (rate * (h - overtime)) + ((rate * 1.5) * overtime)
