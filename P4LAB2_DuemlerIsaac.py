response1 = 1
while response1 == 1:
    print("Enter an integer:", end = " ")
    num = int(input())
    if num < 0:
        print("Cannot except negative values")
    elif num >=0:
        for i in range(13):
            print(f"{num}*{i}={num*i}")
        
    print("Would you like to run this program again?", end= " ")
    response = input()
    if response == ("yes"):
        response1 = 1
    elif response == ("no"):
        response1 = 2

print("Exiting program")
