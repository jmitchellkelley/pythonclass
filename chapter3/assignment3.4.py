#52

#Get Number
numb = input("Enter a telephone number: ")

#math

numb = numb.replace('-',"")
print("Number without dashes is", numb)

#53
vowels = "aeiou"
phrase = input("Enter a phrase: ")
n = 0
for i in phrase:
	if i in vowels:
		n += 1
print("The phrase contains", n, "vowels.")


#54

#Get Numbers from User
x1 = float(input("Enter a number: "))
x2 = float(input("Enter a number: "))
x3 = float(input("Enter a number: "))

#Compare Numbers
if (x1 >= x2) and (x1 >= x3):
	x4 = x1
elif (x2 >= x1) and (x2 >= x3):
	x4 = x2
else:
	x4 = x3

#print
print("Largest number:", x4)

print()

#59

#Get Info
name = input("Enter name: ")
age = int(input("Enter age: "))
ss = int(input("Enter starting salary: "))

#math
total = ss
for i in range (age+1, 65):
	ss += ((ss * 5) / 100)
	total += ss

print(name, "will earn about ${:,.0f}".format(total))
print()

#60
prin = 1000
amount = 0
p = prin
print("\t" + "Simple Interest" + "\t" + "Compound Interest")
for i in range(1,5):
	amount = p*1.05
	p = amount
	print(str(i)+"\t" + "$" + str(prin+ 50 * i) + "\t\t" + "$" + str(round(amount, 2)))

