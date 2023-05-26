nums = [1,2,3]
nums[2] = 100

print(nums) 
nums.append(2)
print(nums)
del(nums[2])
print(nums)

customer_name = input("What is your Name : ")

print(f"Nice To meet You, {customer_name}")

PI = 3.14
r = int(input(f"radius : "))
calcRadius = PI *r**2
print(calcRadius)

person = {}

while True :
    name = input("Your Name : ")
    age = input("Your age : ")
    person["User_name"] = name
    person["User_age"] = age
    again = input("again y/n")
    if again == "y" :
        continue
    else :
        break

for (key,value) in person.items():
    print(f"{key} is {value}")


name = input("Tell Me Your Name : ")

print(f"Hello {name} , Nice to meet you"); 