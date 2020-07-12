# To find out the sum, count and average of a set of values. To end type 'done'

num = 0
tot = 0.0
while True :
    val = input('Enter value: ')
    if val == 'done':
        break
    try:
        fval = float(val)
    except:
        print('Invalid input')
        continue
    num = num + 1
    sum = fval + tot
print("Count:", num)
print("Sum:", sum)
print("Average:", sum/num)
