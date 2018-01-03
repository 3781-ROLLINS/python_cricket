#Simple string
name="Sumeet"
print("hello %s" % name)

#To use two or more argument specifiers, use a tuple (parentheses):
name="Sumeet"
age=22
print("%s is %d years old" % (name,age))

#using list as string
mylist=[1,2,3]
print("A list: %s" % mylist)

#Exercise
data = ("Sumeet", "Pawar", 22)
format_string = "Hello %s %s. Your are %d years old."
print(format_string % data)


#String Operations
name = "Sumeet Pawar"
print(name + " is %d characters long" % len(name))
print("Index of character a is %s" % name.index("a"))
print("No. of 'e' in the string are %s" % name.count("e"))
print(name[::-1])
print("String starts with Sumeet?" name.startswith("Sumeet"))
print(name.endswith("asdf"))