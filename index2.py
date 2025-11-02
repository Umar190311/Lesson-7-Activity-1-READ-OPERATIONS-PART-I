#open first line of file
file = open("Codingal.txt", "r")
print("Reading the first line.... ")
print(file.readline())
file.close()

#read the first three lines of the file
file = open("Codingal.txt", "r")
print("REading the first three lines..")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# looping through all the lines of the files
file = open("Codingal.txt", "r")
print("Looping through the lines..")
for line in file:
    print(file)
file.close()

file = open("Codingal.txt", "r")
print("Reading all the lines..")
for f in file.readlines():
    print(f)
file.close()