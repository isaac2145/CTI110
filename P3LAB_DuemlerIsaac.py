# Isaac Duemler
# 06/16/2025
# P3LAB
# money
print("Enter the amount of money as a float: $", end="")
money = float(input())
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
else:
    print("No change")
