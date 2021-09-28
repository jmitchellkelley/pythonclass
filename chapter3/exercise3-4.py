#Exercise 17

for i in range(1, 5):
	print("Pass #" + str(i))
print()

#Exercise 18

for i in range(3, 7):
	print(2 * i)
print()

#Exercise 29

for ch in "Python":
	continue
print(ch)
print()

#Exercise 32

list1 = [2, 9, 6, 7, 13, 3]
maxOfOdds = 0
for num in list1:
	if (num % 2 == 1) and (num > maxOfOdds):
		maxOfOdds = num
print(maxOfOdds)
print()

#Exercise 58
## Determine if a word contains every vowel.

word = input("Enter a word: ")
word = word.upper()
vowels = "AEIOU"
isVowelWord = True
for letter in vowels:
    if letter not in word:
        isVowelWord = False
        break
if isVowelWord:
    print(word, "is a vowel word.")
else:
    print(word, "is a not a vowel word.")
print()

#Exercise 61
## Display the balances on a car loan.
print("         AMOUNT OWED AT")
print("YEAR    ", "END OF YEAR")   
balance = 15000
year = 2012
for i in range(1, 49):
    balance = 1.005 * balance - 290
    if i % 12 == 0:
        year += 1
        print(year, "    ${0:,.2f}".format(balance))
print(year + 1, "    $0.00")    
print()

