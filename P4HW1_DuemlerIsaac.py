#Isaac Duemler
#07/14/2025
#P4HW1
#score-loops
#pseudocode(detail algorithm)


print("How many scores do you want to enter?", end = " ")
how_many = int(input())
score_num = 1
numbers = []
while 0<how_many<=100:
    print(f"Enter score #{score_num}", end = " ")
    score = int(input())
    if score < 0:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
    elif score >= 0:
        numbers.append(score)
        score_num = score_num + 1
        how_many = how_many - 1
print("------------Results----------")
lowest = min(numbers)
print(f"Lowest score  : {lowest}")
numbers.remove(lowest)
print(f"Modified List : {numbers}")
average = sum(numbers) / len(numbers)
print(f"Scores Average: {average}")
if average >= 90:
    print("Grade         : A")
elif average >= 80:
    print("Grade         : B")
elif average >= 70:
    print("Grade         : C")
elif average >= 60:
    print("Grade         : D")
else:
    print("Grade         : F")
