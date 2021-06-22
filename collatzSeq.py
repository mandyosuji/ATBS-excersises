def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return 3 * number + 1

while True:
    userInput = input("Enter Number:\n")
    try:
        userInt = int(userInput)
        break
    except ValueError:
        print("You must enter an integer value")
        
result = collatz(userInt)

while result != 1:
    print(result)
    result = collatz(result)

print(1)
