file=open("session11.py","r")
""""
line=file.readline()
print(line)
line=file.readline()
print(line)
line=file.readline()
print(line)
line=file.readline()
print(line)
"""
# readline will read a single line
# and next time it will read the next line
lines=file.readlines()
print(lines)
print(len(lines))
print(type(lines))

for line in lines:
    print(line)