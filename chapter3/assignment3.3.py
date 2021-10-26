#23
pri = 15000
ir = 6
mp = 290
bal = pri
n = 0
while True:
	temp = 1.005 * bal - mp
	n = n + 1
	if(temp <= pri / 2):
		break;
	bal = temp
print("Loan will be half paid off after {:.00f} months.".format(n)) 
print()

#24
mp = 100
n = 0
i = 1.0025
endBal = 0
while endBal < 3000:
	endBal = i * (endBal + mp)
	n += 1
print("Annuity will be worth more than $3000 after {:.00f} months.".format(n))
print()

#25
startBal = 10000
i = 1.003
w = 600
n = 0
qBal = startBal
while qBal > 600:
	qBal = i * (qBal - w)
	n += 1
	
print("Balance will be ${:02f} after".format(qBal), "after", n, "months.")
print()

#31
startBal = 1000
print("Options:")
print("1. Make a Deposit")
print("2. Make a Withdrawal")
print("3. Obtain Balance")
print("4. Quit")

while(True):
	n = input("Make a selection from the options menu: ")
	if (n=='1'):
		dep = int(input("Enter amount of deposit: "))
		startBal = startBal + bal
		print("Deposit Processed")
	elif (n=='2'):
		while(True):
			withd = int(input("Enter amount of withdrawal: "))
			if(withd > startBal):
				print("Denied. Maximum withdrawal is ${:.02f}".format(startBal))
				continue
			startBal = startBal - withd
			break
		print("Withdrawal Processes.")
	elif (n=='3'):
		print("Balance: ${:.02f}".format(startBal))
	else:
		break
print()

