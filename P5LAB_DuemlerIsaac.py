#Isaac Duemler
#07/19/2025
#P5LAB
#checkout

import random
owe = round(random.uniform(0.01, 100.00), 2)
print(f"You owe ${owe}")
print("How much cash will you put in the self-checkout?", end = " ")
cash = float(input())
money = cash - owe

print(f"Change is: ${money:.2f}")
cents = int(money * 100)
dollars = cents//100
quarters = (cents-(dollars*100))//25
dimes = (cents-((quarters*25)+(dollars*100)))//10
nickels = (cents-((quarters*25)+(dollars*100)+(dimes*10)))//5
pennies = (cents-((dollars*100)+(quarters*25)+(dimes*10)+(nickels*5)))//1
if dollars == 1:
    print(dollars, "dollar")
if dollars > 1:
    print(dollars, "dollars")
if quarters == 1:
    print(quarters, "quarter")
if quarters > 1:
    print(quarters, "quarters")
if dimes == 1:
    print(dimes, "dime")
if dimes > 1:
    print(dimes, "dimes")
if nickels == 1:
    print(nickels, "nickel")
if nickels >1:
    print(nickels, "nickels")
if pennies == 1:
    print(pennies, "penny")
if pennies > 1:
    print(pennies, "pennies")
if money == 0:
    print("No change")

