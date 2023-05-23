# def greet(name):
#     print("Good Morning My Neighbour,I am : " + name)

# greet("Sai Yan Naing")

# def greet (name = "Aung", time = "night"):
#     print(f'Good {time} {name}')

# greet(time= "morning", name ="Sai")

name = "Sai"

def sayMyName() :
    global name
    name = "Yan Naing"
    print(name)

sayMyName()
print(name)