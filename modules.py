import random

def divideNumbers(divideFirst, divideSecond):
    numberList = (range(1, 1001))
    array = []
    for x in numberList:
        if x % divideFirst == 0 and x % divideSecond == 0:
            array.append(x)
            total = 0
            for x in array:
                total += x
    print(array)
    print("Medelvärdet är", total / len(array))

def randomTal(firstNumber = 1, secondNumber = 100):
    maxAttempts = secondNumber // 3
    print(f"\n\nGissa rätt tal mellan {firstNumber}-{secondNumber}, du har max {maxAttempts} försök.")
    print("Avbryt med 0")
    guess = 0
    attempt = 0
    number = random.randint(firstNumber, secondNumber)
    while guess != number:
        guess = userInputInt()
        if guess == 0:
            break
        if guess < number:
            print("Talet är större")
        elif guess > number:
            print("Talet är mindre")
        elif guess == number:
            print("\nWow! Du har vunnit!")
            break
        attempt += 1
        if attempt == maxAttempts:
            print("\nDu har förlorat...")
            break

def userInputInt():
    while True:
        try:
            x = int(input("Ange en siffra: "))
            break
        except:
            print("Error, inte giltig siffra, försök igen")
    return x