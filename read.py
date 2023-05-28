file = open("./text.txt")

for line in file :
    print(line)
file.seek(0)
reader=file.readlines()
print(reader)

file.seek(50)
para = file.read(100)
print(para)
file.close()

with open("./text.txt") as file:
    for line in file:
        print(line)