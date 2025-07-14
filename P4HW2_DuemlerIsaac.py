# Isaac Duemler
# 07/14/2025
# P3HW2
# finance_loops
# pseudocode(detail algorithm)
name = "name"
number_employees = 0
total_overtime = 0
total_regular = 0



while name != "Done":
    name = input("Enter employee's name or Done to terminate:")
    if name != "Done":
        hours = float(input(f"How many hours did {name} work?"))
        pay = float(input(f"What is {name}'s pay rate:"))
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
        number_employees = number_employees + 1
        total_overtime = total_overtime + overtime_pay
        total_regular = total_regular + regular_pay



print(f"Total number of employees entered: {number_employees}")
print(f"Total amount paid for overtime: {total_overtime}")
print(f"Total amount paid for regular hours: {total_regular}")
print(f"Total amount paid in gross: {total_overtime + total_regular}")
