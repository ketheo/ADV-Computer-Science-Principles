import random

def secretCode():
  for n in range(4):
    secretNumbers.append(random.randint(1, 10))
  print(secretNumbers)
  

def getGuesses():
  guessedNumbers.clear()
  for i in range(4):
    guessedNumbers.append(int(input("Enter your " + str(i + 1) + " guess: ")))


def checkGuesses():
  countCorrect = 0
  for i in range(4):
    if guessedNumbers[i] == secretNumbers[i]:
      countCorrect += 1
  print("You have ", countCorrect, " correct and in the right spot out of 4.")
  return countCorrect

  

# *** MAIN ***

secretNumbers = []
guessedNumbers = []
tries = 0
countCorrect = 0

secretCode()

while countCorrect < 4:
  getGuesses()
  countCorrect = checkGuesses()
  tries += 1
  if countCorrect == 4:
    print("It took you", tries, "tries to get them all.")
