#To count the number of lines in a file starting with a specific word
fname = input("Enter file name: ")
fh = open(fname)

count = 0
x = input("Enter the word that the line starts with: ")

for line in fh:
    if line.startswith(x):
        count = count + 1
        lin = line.strip()
        print(lin)



print("There were", count, "lines in the file with", x, "as the first word")
