#97

#Input from user
n = float(input("Enter number of seconds between lightning and thunder: "))

d = (n / 5)

#Display
print("Distance from storm: {:.2f} miles.".format(d))

print()

#98

#Get numbers
a = int(input("Enter your age: "))
r = int(input("Enter your resting heart rate: "))

#Math
thr = (.7 * (220 - a) + .3 * r)

#display
print("Your training heart rate is:", thr, "beats/min.")

print()

#99

#get numbers
c = float(input("Enter a number of hours cycling: "))
r = float(input("Enter a number of hours running: "))
s = float(input("Enter a number of housr swimming: "))

#math
calories = ((c * 200) + (r * 475) + (s * 275))
pounds = (calories / 3500)

#print
print("Weight loss:", pounds, "pounds")

print()

#100

#get numbers
w = float(input("Enter wattage: "))
hu = float(input("Enter number of hours used: "))
kWh = float(input("Enter price per kWh in cents: "))

#math
cost = ((w * hu) / (1000 * kWh))

#display
print("Cost of electrictiy: ${:.2f}".format(cost))

print()

#111

#get months
wm = int(input("Enter a number of months: "))

#math
y = (wm // 12)
m = (wm % 12)

#print
print(wm, "months is", y, "years and", m, "months.")
