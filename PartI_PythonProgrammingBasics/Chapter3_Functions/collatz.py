def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Enter number:')
try:
    userInput = int(input())
    while userInput != 1:
        userInput = collatz(userInput)
except:
    print('you must enter an integer')
