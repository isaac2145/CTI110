#Isaac Duemler
#06/27/2025
#P2LAB2
#Dictionary uses
cars = {"Camaro": 18.21,
        "Prius": 52.36,
        "Model S": 110,
        "Silverado": 26}
keys = cars.keys()
print(keys)
print("Enter a vehicle to see it's mpg:", end=" ")
search = input()
print(f"The {search} gets {cars[search]} mpg.")
print("How many miles will you drive the Prius?", end=" ")
miles = float(input())
mpg = cars[search]
gallons_needed = miles / mpg
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the Prius {miles} miles.")
