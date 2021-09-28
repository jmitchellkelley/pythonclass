#Chapter 2 Test
#Mitch Kelley
#DSS 325

#1. Make Change

#Ask User for Cents Input
coins= int(input("Enter an amount of change: "))

#Make Change and Display

print(coins//25, "quarters")
coins= coins%25

print(coins//10, "dimes")
coins= coins%10

print(coins//5, "nickles")
coins= coins%5

print(coins//1, "pennies")

print()


#2. Car Loan

#Ask User for Loan Values and Years

loan= int(input("Enter amount of your loan: "))
r= float(input("Enter interest rate (%): "))
y= int(input("Enter number of years: "))

#Perform Calc

i= (r / 1200)
mp= ((i/(1 - ((1 + i) ** (-12 * y))) * loan))

#Display Monthly Payments

print("Monthly Payment: ${0:.2f}".format(mp))

print()


#3. Bond Yield

#Collect Info for Bond

bond= int(input("Enter face value of bond: "))
r= float(input("Enter coupon interest rate: "))
mp= int(input("Enter current market price: "))
y= int(input("Enter years until maturity: "))

#Perform Calc

a= ((bond - mp) / y)
b= ((bond + mp) / 2)
intr= (bond * r)
ytm= ((intr + a) / b)

#Display YTM

print("Approximate YTM:", "{0:.2%}".format(ytm))

print()

