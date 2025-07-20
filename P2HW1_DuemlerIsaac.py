#IsaacDuemler
#06/27/2025
#P2HW1
#changingP1HW2
print("This program calculates and displays travel expenses")
print("Please enter your budget:", end=" ")
budget = int(input())
print("Please enter travel destination:", end=" ")
dest = input()
print("How much do you think you will spend on gas?", end=" ")
gas = float(input())
print("Approximately, how much will you need for accomodation?", end=" ")
hotel = float(input())
print("Last, how much do you need for food?", end=" ")
food = float(input())
expenses = gas+food+hotel
remainder = budget-expenses
text = ""
right_padded1 = text.rjust(15, ' ')
right_padded2 = text.rjust(5, ' ')
right_padded3 = text.rjust(9, ' ')
print("-------------Travel Expenses-------------")
print(f"location: {right_padded3} {dest:30}")
print(f"Initial Budget:{right_padded2}${budget:.2f}")
print(f"Fuel:{right_padded1}${gas:.2f}")
print(f"Accomodation: {right_padded2} ${hotel:.2f}")
print(f"Food:{right_padded1}${food:.2f}")
print("-----------------------------------------")
print(f"Remaining Balance:  ${remainder:.2f}")


