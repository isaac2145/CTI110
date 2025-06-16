# Isaac Duemler
# 06/16/2025
# P1HW2
# basic math

print("This program calculates and displays travel expenses")
print("Please enter your budget:", end=" ")
budget = int(input())
print("Please enter travel destination:", end=" ")
dest = input()
print("How much do you think you will spend on gas?", end=" ")
gas = int(input())
print("Approximately, how much will you need for accomodation?", end=" ")
hotel = int(input())
print("Last, how much do you need for food?", end=" ")
food = int(input())
expenses = gas+food+hotel
remainder = budget-expenses
print("-------------Travel Expenses-------------")
print("location:", dest)
print("Initial Budget:", budget)
print("")
print("Fuel:", gas)
print("Accomodation:", hotel)
print("Food:", food)
print("")
print("Remaining Balance:", remainder)

# program Pseudocode (logic)
