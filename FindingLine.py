#To find a line by its starting word. Please make sure to enter the files correctly, keeping in mind the directory

fname = input("Enter file name: ")
fh = open(fname)
count = 0
x = input("Enter the starting word of the line you want to find: ")
for line in fh:
    if line.startswith(x) :
        count = count + 1
        print(line)
