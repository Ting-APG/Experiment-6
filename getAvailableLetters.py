def getAvailableLetters(lettersGuessed):
        import string
        lowercases = string.ascii_lowercase
        LA=  []
        for y in lowercases:
            if y not in lettersGuessed:
                LA += y
        return LA
    