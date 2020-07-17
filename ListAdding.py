#This is for adding words of a file in a list, in alphabetical order
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
fs = fh.read()
fss = fs.rstrip()
lst = fss.split()
res = []
for i in lst:
    if i not in res:
        res.append(i)
res.sort()
print(res)
