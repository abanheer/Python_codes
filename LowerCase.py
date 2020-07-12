# To change the text case of any file to Lower Case
fname = input("Enter file name: ")
fh = open(fname)
ttt = fh.read()
tttt = ttt.rstrip() #To remove extra \n
tt = tttt.lower()  #To lowercase the text
print(tt)
