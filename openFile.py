import os

a = 10
print(a)
file = open('Mydata.txt', 'r')

print(file.read())

#creating a new file
# newFile = open("newFileCreated.txt", "w")
# newFile.write("This is a new content")

os.remove("newFileCreated.txt")