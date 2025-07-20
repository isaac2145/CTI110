#Isaac Duemler
#06/28/2025
#P2HW2
#grades
grades = []
print("Enter grade for module 1", end=" ")
module1 = float(input())
grades.append(module1)
print("Enter grade for module 2", end=" ")
module2 = float(input())
grades.append(module2)
print("Enter grade for module 3", end=" ")
module3 = float(input())
grades.append(module3)
print("Enter grade for module 4", end=" ")
module4 = float(input())
grades.append(module4)
print("Enter grade for module 5", end=" ")
module5 = float(input())
grades.append(module5)
print("Enter grade for module 6", end=" ")
module6 = float(input())
grades.append(module6)
average = sum(grades)/6
print("----------Results---------")
print("Lowest Grade: ", min(grades))
print("Highest Grade:", max(grades))
print("Sum of Grades:", sum(grades))
print(f"Average:       {average:.2f}")
print("--------------------------")
