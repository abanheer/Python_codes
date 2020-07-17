#This is to find all the numerical values in a file and add them
import re
val = 0
name = input("Enter file:")
handle = open(name)
hand = handle.read()
y = re.findall('[0-9]+',hand)
for nus in y:
    val = val + int(nus)

print("The total value of the numbers is", val)
