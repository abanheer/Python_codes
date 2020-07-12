# To change the text case of any file to Upper Case
fname = input("Enter file name: ")
fh = open(fname)
ttt = fh.read()
tttt = ttt.rstrip() #To remove extra \n
tt = tttt.upper()  #To uppercase the text
print(tt)
