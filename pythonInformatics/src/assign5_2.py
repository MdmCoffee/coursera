largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == "done":
            break
        else:
            num = int(num)
            if largest is None or num > largest:
                largest = num

            if smallest is None or num < smallest:
                smallest = num
    except:
        print 'Invalid input'

print "Maximum is ", largest
print "Minimum is ", smallest
