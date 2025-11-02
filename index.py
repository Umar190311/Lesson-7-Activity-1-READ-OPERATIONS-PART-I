# open file and read its content
file = open("Codingal.txt", "r")
print(file.read())
file.close

# open file and read its beginning 8 characters
file = open("Codingal.txt", "r")
print("\n Read in parts \n")
print(file.read())
file.close

# append your name and age in the file 
file = open("Codingal.txt","a")
file.write(" HHi I am Umar and I am of 14 years old")
file.close