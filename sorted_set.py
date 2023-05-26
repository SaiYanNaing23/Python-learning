# nums = [2,6,4,6,90,7,2,1,4,6,7]

# print(sorted(nums))

# names = ["Kyaw","Aung", "aung", "blah blah"]

# print(sorted(names))


# Example usage:
# coupon_codes = list(generate_coupon_code())
# for coupon in set(coupon_codes) :
#     print(sorted(coupon))

# import random
# prefix = "CO"
# def generate_coupon_code():
    
#     nums = random.randint(1, 999999)  # Generate a random number with six digits
#     return  f"{prefix}{nums}"  # Format the number with leading zeros
    

# # Example usage:
# coupon_code = generate_coupon_code()
# print(coupon_code)

# ages = [20,40,50,20]

# for age in set(ages) :
#     print(age)

person = {}

while True:
    name = input("Your Name : ")
    age = input('Your aage : ')
    person[name] = age
    another = input("again Y/N")
    if another == "Y" :
        continue
    else :
        break

ages = list(person.values())

for age in ages :
    count = ages.count(age)
    print(f"{age} years old - {count}")