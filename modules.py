import random

def divideNumbers(divideFirst, divideSecond):
    numberList = range(1, 1001)
    array = []
    total = 0
    for x in numberList:
        if x % divideFirst == 0 and x % divideSecond == 0:
            array.append(x)
            total += x
    
            
    print(array)
    print("Medelvärdet är", total / len(array))


def randomTal(firstNumber = 1, secondNumber = 100):
    number = random.randint(firstNumber, secondNumber)
    maxAttempts = secondNumber // 3
    guess = 0
    attempt = 0
    print(f"\n\nGissa rätt tal mellan {firstNumber}-{secondNumber}, du har max {maxAttempts} försök.")
    print("Avbryt med 0")
    #fusk > print(number)
    
    while guess != number:
        guess = userInputInt()
        attempt += 1
        if guess == 0: # avsluta
            break
        elif guess < number:
            print("Talet är större")
        elif guess > number:
            print("Talet är mindre")
        elif guess == number:
            print("\nWow! Du har vunnit!")
            break
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