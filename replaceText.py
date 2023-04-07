filename = input("Enter a filename: ")

f = open(filename, "r")
file = f.readlines()
f.close()

    
oldstring = input("Enter the old string to be replaced: ")
newstring = input("Enter the new string to replace the old string: ")
index = 0
for line in file:
    if oldstring in line:
        newLine = line.replace(oldstring, newstring)
        file[index] = newLine
    index +=1              
f = open(filename, "w")
f.writelines(file)
f.close()
print("Done")
