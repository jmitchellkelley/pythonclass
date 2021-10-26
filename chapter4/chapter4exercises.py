##Classwork

#5
def main():
	taxableIncome = 16000
	print("Your income tax is ${0:,.2f}".format(stateTax(taxableIncome)))

def stateTax(income):
	## Calculate state tax for a single resident of Kansas
	if income <= 15000:
		return .03 * income
	else:
		return 450 + (.049 * (income - 15000))
main()
print()

#7
def main():
	question()
	answer()

def answer():
	print("Because they were invented in the northern")
	print("hemisphere where sundials go clockwise.")

def question():
	print("Why do clocks run clockwise?")
	print()

main()
print()

#14
x = 7

def main():
	global x
	x = 5
	f()
	print(x)

def f():
	print(x)

main()
print()

#PG 147 Top Part
def triple(num):
	num = 3 * num
	return num

num = 2
print(triple(num))
print(num)
print()

#17
SALES_TAX_RATE = 0.06

def main():
	price = 100
	cost = (1 + SALES_TAX_RATE) * price
	print("Total cost: ${0:,.2f}".format(cost))
main()
print()

#19
def main():
	num = 5
	triple(num)
	print(num)

def triple(num):
	num = 3 * num

main()
print()

#22
def main():
	grades = [80, 75, 90, 100]
	grades = dropLowest(grades)
	average = sum(grades) / len(grades)
	print(round(average))

def dropLowest(grades):
	lowestGrade = min(grades)
	grades.remove(lowestGrade)
	return grades

main()
print()
