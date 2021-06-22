def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

gotInt = False
while not gotInt:
    userInput = input("Enter Number:\n")
    try:
        userInt = int(userInput)
        gotInt = True
    except ValueError:
        print("You must enter an integer value")
        
result = collatz(userInt)

while result != 1:
    print(result)
    result = collatz(result)

print(1)
