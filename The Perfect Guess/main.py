import random
n = random.randint(1,100)

a=-1
guesses = 0
while(a!=n):
    a = int(input("Enter the number you want to guess : "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")
    guesses = guesses+1
print(f"You take {guesses} chances to guess number {n}")