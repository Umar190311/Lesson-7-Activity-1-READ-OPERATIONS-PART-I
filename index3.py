# Program to remove the lines starting with any prefix
file1 = open("Codingal.txt", "r")
file2 = open("bmm.txt", "w")

#reading each line from original
for line in file1.readlines():

    #reading all lines that do not begin with "Coding"
    if not (line.startswith("Coding")):

        #printing those lines
        print(line)

        #storing only those lines that do not begin with "Coding"
        file2.write(line)

#close and save the file
file2.close()
file1.close()
