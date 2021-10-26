##Exam 2
##Mitch Kelley
##Open Source Programming
##22 Oct. 2021

#Question1
#Get Info
loan = float(input("Enter the amount of the loan: "))
ir = float(input("Enter the interest rate: "))
month = int(input("Enter the duration in months: "))

#Check Data and math
if loan < 0 or ir < 0 or ir > 100 or month < 0:
	print("Invalid Data. Please try again.")
	quit()
else:
	ir = (float(ir) / 12) / 100
mp = (loan * ir) / (1 - ((1 + ir) ** (-1 * month)))

ti = month * mp - loan
ti = round(ti, 0)

#Display
print("Monthly payment: ${:.02f}".format(mp))
print("Total interest paid: ${:.02f}".format(ti))
print()

#Question5
#Math
def annual_interest(amt, int, period, year):
	r = 1 + (int / period)
	n = period * year
	return amt * (r ** n)

deposit = 5000
e = deposit * 15
l = deposit * 33

x = 0
for n in range(15):
	x = x + deposit
	x = annual_interest(x, 0.04, 1, 1)
x = annual_interest(x, 0.04, 1, 32)

y = 0
for n in range(32):
	y = y + deposit
	y = annual_interest(y, 0.04, 1, 1)
y = y + deposit

#Print
print("\t\tAMOUNTS DEPOSITED")
print("Earl: ${:,.02f} \t\tLarry: ${:,.02f}".format(e, l))
print("\tAMOUNTS IN IRA UPON RETIREMENT")
print("Earl: ${:,.02f} \t\tLarry: ${:,.02f}".format(x, y))
print()

#Question6
#Logic
def code_logic(n):
    number = "" 
    if n in "bfpv":
        number = "1"
    elif n in "cgjkqsxz":
        number = "2"
    elif n in "dt":
        number = "3"
    elif n == "l":
        number = "4"
    elif n in "mn":
        number = "5"
    elif n == "r":
        number = "6"
    
    return number

def soundex(word):
    if len(word) == 0:
        return "0000"
    result = word[0]
    word = word.lower()
    for n in "aeiouhyw":
        word = word.replace(n, " ")
    for i in range(1, len(word)):
        if word[i].isalpha():
            number = code_logic(word[i])
            if number != code_logic(word[i - 1]):
                result += number
        if len(result) == 4:
            break

    while len(result) < 4:
        result += "0"
    return result

word = input("Enter a word to code: ")
print("The coded word is {}.".format(soundex(word)))
