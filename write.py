with open("about.txt","w") as file:
    file.write("Sai Yan Naing")

with open("./about.txt","a") as file:
    file.write("\nI am 21 years old")

lists = ["Sai Yan Naing","\nI am 21 years old"]

with open("about.txt","w") as file:
    file.writelines(lists)