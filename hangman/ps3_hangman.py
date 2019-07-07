# Hangman game
# 

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

# IMPORTANT: ADJUST YOUR PATH ACCORDINGLY
WORDLIST_FILENAME = "C:/Users/elope/Desktop/hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(str(len(wordlist)) + " words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    guess = ''.join(lettersGuessed)
    if secretWord == guess:
        return True
    
    l = len(secretWord)
    count = 0
    for index in range(0,l):
        if secretWord[index] in lettersGuessed:
            count += 1
            
    if l == count:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    result = []
    l = len(secretWord)
    
    for index in range(0,l): 
        if secretWord[index] in lettersGuessed:            
            result.append(secretWord[index])
        else:
            result.append('_')

    return ''.join(result)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    libraryList = list(str(string.ascii_lowercase))

    l = len(lettersGuessed)
    for index in range(l): 
        if lettersGuessed[index] in libraryList:            
            libraryList.remove(str(lettersGuessed[index]))
            
    return ''.join(libraryList)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses = 8                 # User has 8 chances to be wrong.
    allLettersGuessed = []      # Will store all of the player's guesses

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-----------")
    
    while (guesses >= 1):
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(allLettersGuessed))

        letter = input("Please guess a letter: ")
        letterInLowerCase = letter.lower()          # Convert to lowercase

        if letterInLowerCase in secretWord and letterInLowerCase in getAvailableLetters(allLettersGuessed):
            allLettersGuessed.append(letterInLowerCase) # Add to the end of the list of guesses
            print("Good guess: " + getGuessedWord(secretWord, allLettersGuessed))
        elif letterInLowerCase in allLettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, allLettersGuessed))
        else:
            guesses -= 1
            allLettersGuessed.append(letterInLowerCase) # Add to the end of the list of guesses
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, allLettersGuessed))

        print("-----------")

        if isWordGuessed(secretWord, allLettersGuessed):   #Returns True or False
            print("Congratulations, you won!")
            break

    if (guesses == 0):
        print("Sorry, you ran out of guesses. The word was " + secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
