def getGuessedWord(secretWord,lettersGuessed):
    Z = []
    for x in secretWord:
        if x in lettersGuessed:
             Z += x
        else:
             Z += "_"
    return Z