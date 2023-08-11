import random


n = int(input())
a = random.randint(1, n)
print(a)

while True:
    guess = int(input())
    if guess <= 0:
        print("Sorry that you're giving up!")
        break
    if guess > a:
        print("Number is too large")
        continue
    if guess < a:
        print("Number is too small")
        continue
    else:
        print("Congratulation. You made it!")
        break
