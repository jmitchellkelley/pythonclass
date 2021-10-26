#53

#get info
bill = float(input("Enter amount of bill: "))
tip = float(input("Enter percentage tip: "))

#math
tip = (tip / 100)
tip = (bill * tip)
print("Tip: ${:.02f}".format(tip))
print()

#54

#get info
rev = float(input("Enter revenue: "))
exp = float(input("Enter exepenses: "))

#math
inc = (rev - exp)
print("Net income: ${:.02f}".format(inc))
print()

#55

#get info
s1 = int(input("Enter beginning salary: "))

#math
s2 = (s1 * 1.1)
s3 = (s2 * .9)
c = ((s3 -s1) / s1 * 100)
print("New salary: ${:.02f}".format(s3))
print("Change: {:.02f}%".format(c))
print()

#56

#get

s1 = int(input("Enter beginning salary: "))

#math

s2 = (s1 * 1.05)
s3 = (s2 * 1.05)
s4 = (s3 * 1.05)
c = (((s4 - s1) / s1) * 100)
print("New Salary: ${:.02f}".format(s4))
print("Change: {:.02f}%".format(c))
print()

#57

#get
p = float(input("Enter principal: "))
ir = float(input("Enter interest rate (as %): "))
yrw = float(input("Enter number of years: "))

#math

step1 = (ir / 100)
step2 = (1 + step1)
step3 = (step2 ** yrw)
step4 = (p * step3)
print("Future value: ${:.02f}".format(step4))
