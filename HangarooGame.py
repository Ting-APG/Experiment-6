def isWordGuessed(secretWord,lettersGuessed):
    for s in secretWord:
        if s not in lettersGuessed:
            return False
    return True
def getGuessedWord(secretWord,lettersGuessed):
    Z = []
    for x in secretWord:
        if x in lettersGuessed:
             Z += x
        else:
             Z += "_"
    return Z
def getAvailableLetters(lettersGuessed):
        import string
        lowercases = string.ascii_lowercase
        LA=  []
        for y in lowercases:
            if y not in lettersGuessed:
                LA += y
        return LA
    
def HangaroosGame(secretWord):
    secretWord = secretWord.lower()
    print ('welcome to the game called Hangaroo')
    print ('I am thinking of the a word that has', len(secretWord) ,'letters, You have 5 tries or you will be hanged')
    lettersGuessed = []
    mistakesMade = 0
    live = 5
    while mistakesMade != 5:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print ("Congratulations! You've won!")
            break
        print("Available letters left: ", getAvailableLetters(lettersGuessed))
        lives = live - mistakesMade
        print("Lives Left: ",lives)
        A = str(input('Enter the letter that you want to guess ')).lower()
        if A in secretWord and A not in lettersGuessed:
            lettersGuessed += A
            print("good JOB! you have guessed a correct letter", getGuessedWord(secretWord,lettersGuessed))
        elif A in lettersGuessed:
                      print("You have already used this letter, Please Try Again ", getGuessedWord(secretWord,lettersGuessed))
        else:
            print("That letter is not included: ", getGuessedWord(secretWord,lettersGuessed))
            lettersGuessed += A
            mistakesMade += 1 
        if mistakesMade == 5:
            print ("Sorry, You've ran out of Lives left and you will be Hanged. The word was ",  secretWord)
            break
        else: 
            continue