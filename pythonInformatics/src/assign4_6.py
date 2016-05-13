def computepay(h,r):
    if h <= 40:
        return h * rate
    else:
        overtime = h - 40
        return (rate * (h - overtime)) + ((rate * 1.5) * overtime)

hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))

print computepay(hrs,rate)
