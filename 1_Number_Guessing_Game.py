import random
ans = random.randint(0,100)
check = False
while check == False:
  guess = int(input("Guess a number between 0 and 100: "))
  if guess == ans:
    print("You guessed it! The number was", ans)
  elif guess<ans:
    print("Too low! Try again!")
  elif guess>ans:
    print("Too high! Try again!")
  else:
    print("Enter a number between 1 to 100")