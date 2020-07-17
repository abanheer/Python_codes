di = dict()
name = input("Enter file:")
handle = open(name)
for line in handle:
    for word in line.split():
        di[word] = di.get(word,0)+1

#Finding most common word
largest = -1
wor = None
for k,v in di.items():
    if v > largest :
        largest = v
        wor = k

print("The most commonly occuring word is", wor, "appearing", largest, "times")
