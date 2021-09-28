#Exercise 1
num = 3
while True:
	num = 2 * num
	if num > 15:
		break
print(num)

print()

#Exercise 2
num = 3
while num < 15:
	num += 5
print(num)

print()

#Exercise 7 - With List

list1 = ['a', 'b', 'c', 'd', 'e']
i = 0
while True:
	print(list1[i])
	i += 1
	if i == len(list1):
		break
#prints the letter of the list corresponding to the number associated with i, adds 1 to i, then checks to see if i is equal to list length, if so breaks.



