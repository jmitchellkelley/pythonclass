#61

name = input("Enter name with two parts: ")
L = name.split()
print("{0:s}, {1:s}".format(L[1], L[0]))

print()

#62
name = input("Enter name with three parts: ")
L = name.split()
print(L[0], L[2])

print()

#63
name = input("Enter name with three parts: ")
L = name.split()
print("Middle Name: ", L[1])

print()

#64
list1 = ['h', 'o', 'n', 'P', 'y', 't']
list2 = list1[3:] + list1[:3]
print(("").join(list2))

print()

#65
tuple1 = ("course", "of", "human", "events", "When", "in", "the")
tuple2 = tuple1[4:] + tuple1[:4]
print((" ".join(tuple2)))

print()

#69
motto = ["e", "pluribus", "unum"]
print(("**").join(motto))

print()

#70
allDay = "around-the-clock"
print(allDay.split('-'))

print()
