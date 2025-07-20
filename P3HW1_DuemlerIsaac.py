# Isaac Duemler
# 06/16/2025
# P3HW1
# program bugs


# This program takes a number grade , determines average and displays
# letter grade for average.

# Enter grades for six modules
print("Enter grade for module 1:", end=" ")
mod_1 = float(input())
print("Enter grade for module 2:", end=" ")
mod_2 = float(input())
print("Enter grade for module 3:", end=" ")
mod_3 = float(input())
print("Enter grade for module 4:", end=" ")
mod_4 = float(input())
print("Enter grade for module 5:", end=" ")
mod_5 = float(input())
print("Enter grade for module 6:", end=" ")
mod_6 = float(input())

# add grades entered to a list

grades =(mod_1, mod_2, mod_3, mod_4, mod_5, mod_6)
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum1 = sum(grades)
avg = round(sum1/6, 2)
print("--------Results--------")
print("Lowest Grade: ", low)
print("Highest Grade:", high)
print("Sum of Grades:", sum1)
print("Average:"," "," "," ", avg)
print("-----------------------")

# determine letter grade for average


if avg >= 90:
    print("Your grade is: A")
elif avg >= 80:
    print("Your grade is: B")
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F") # TO DO: finish this





