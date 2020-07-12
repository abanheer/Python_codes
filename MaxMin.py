#Enter a set of values to find out the maximum and minimum out of them. To end type 'done'

largest = float('-inf')
smallest = float('inf')
while True:
    val = input("Enter a number: ")
    if val == "done" :
        break
    try:
        fval = float(val)
    except:
        print("Invalid input")
        continue
    val = int(val)
    for lval in val :
        if largest is None :
            largest = lval
        elif lval > largest :
            largest = lval
        print(largest, lval)
    for sval in val :
        if smallest is None :
            smallest = sval
        elif sval < smallest :
            smallest = sval
        print(smallest, sval)

print("Maximum", largest)
print("Minimum", smallest)
