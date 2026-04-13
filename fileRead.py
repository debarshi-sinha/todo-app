fileNames = ["a.txt","b.txt","c.txt"]

for fileName in fileNames:
    file = open(f"./files/{fileName}","r")
    print(file.read())
    file.close()