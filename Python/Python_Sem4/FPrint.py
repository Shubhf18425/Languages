name = "shubhhhhh"
age = 20

# print("Hello , %s"    % name)

# print("Hello , %s your age is %s"    % (name , age))

# print("Hello , %s your age is %d"    % (name , age))

# print("Heloo {} yous age is {}".format(name , age))


person = {
    "name" : "shubham",
    "age" : 21
}

# print( "Hello {name} your age is {age}".format(name = person['name'] , age = person['age']))

# print( "Hello {name} your age is {age}".format(**person))

# print("Hello {name} your age is {age}")

# print(f"Hello {name} your age is {age}")

# print(f"{2+10}")

# print(f"2+10")
# hello

def uppercase(name):
    return name.upper()

print(f"Hello {uppercase(name)} your age is {age}")

print(f"Hello {name.upper()} your age is {age}")

print("Hello {name.upper()} your age is {age}")


name = "Eric"
profession = "comedian"
affiliation = "Monty Python"
message = (  f'Hi {name}. '  f"You are a {profession}.     You were in {affiliation}.")
print(message)