person = {
    "name" : "Sai Yan naing",
    "age" : 21,
}

print(person)
print(person["name"])
person["hair_color"] = "black"
print(person)
print("hair_color" in person)

person_key = list(person.keys())
print(person_key)

person_values = list(person.values())
print(person_values)