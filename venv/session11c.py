file=open("session11.py","r")
print(type(file))
print()
fileContents=file.read()
print(type(fileContents))
print()
print(fileContents)
print()
print(len(fileContents))

# Re-Read the File
fileContents = file.read() # Re-Read
print(fileContents)


# Once a File is Opened and Read, we cannot re-read it !!
# You need to re-open and re-read

# HW: Read a Python File and Create a Dictionary which will
# tell us how many classes and Objects exist
# Keys will be Class Name and Values will be Object Count
