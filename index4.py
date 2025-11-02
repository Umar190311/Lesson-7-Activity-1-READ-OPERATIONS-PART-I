#Program to copy odd lines of one file to another
# open file in read mode
fn = open("Codingal.txt", "r")

#open other file inwrite mode
fn1 = open("imm.txt", "w")

#read the content of the file line by line
cont = fn.readlines()
#type(cont)
#print (len(cont))
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fn1.write(cont[i-1])
    else:
        pass
#close the file
fn1.close()

#open file in read mode
fn1 = open("imm.txt", "r")

#read the content of the file
cont1 = fn1.read()

#close all files
fn.close()
fn1.close()