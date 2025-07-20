# Isaac Duemler
# 06/16/2025
# P3HW2
# formatting
# pseudocode(detail algorithm)

name = input("Name of employee:")
hours = float(input("Number of hours worked this week:"))
pay = float(input("Employees pay rate:"))
if hours > 40:
    overtime = hours-40
    overtime_pay = overtime*1.5*pay
    regular_pay = hours*pay
    total_pay = regular_pay + overtime_pay
else:
    regular_pay = hours*pay
    total_pay = hours*pay
    overtime = 0.0
    overtime_pay = 0.0
    

print("-------------------------------")
print("Employee name:", name)

print("Hours Worked   Pay Rate   Overtime   Overtime Pay   RegHour Pay   Gross pay")
print("----------------------------------------------------------------------------")
print(f"{hours:<15.2f}{pay:<11.2f}{overtime:<11.2f}${overtime_pay:<14.2f}${regular_pay:<13.2f}{total_pay:<12.2f}")
    
