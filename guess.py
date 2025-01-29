#Number guessing game

a = 10

b = int (input("Enter guess: "))

while a != b :
    if b>a:
        print("Guess is too high")
        b = int (input("Enter guess again: "))
    elif b<a:
        print("Guess is too low")
        b = int (input("Enter guess again: "))

print("Number found , success")
     
    
