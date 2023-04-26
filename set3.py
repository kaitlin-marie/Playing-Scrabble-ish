print("\033c")



# helper code chunk 

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HandSize = 7

LetterValues = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "wordlist.txt"

def load_words():
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
    print("... words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# end of helper code


wordlist = load_words()

# tests basic scoring
Word = input('Enter your favorite word!')


# scoring
# assumes word is valid
#assigns values to letters and calculates score
def Scoring(Word, HandSize):
    Score = 0
    for e in Word:
        Score += LetterValues[e]
    Score = Score*(len(Word))
    if len(Word) == HandSize:
        Score += 50
        print('Score for this word: ', Score)
        return Score
    else:
        print('Score for this word: ', Score)
        return Score

Score = Scoring(Word, HandSize)    


# displays letters in hand 
def DispHand(Hand):
    for letter in Hand.keys():
        for j in range(Hand[letter]):
             print(letter, end=' ')              # print all on the same line
    print('     ')



# creates random hand with certain amount of vowels
def Deal(HandSize):
    Hand={}
    num_vowels = HandSize // 3
    for e in range(HandSize):
        if e < num_vowels:
            x = random.choice(VOWELS)
        else:
            x = random.choice(CONSONANTS)
        Hand[x] = Hand.get(x, 0) + 1
        
    return Hand


# updates hand by removing letters you've used
def UpdateHand(Hand, Word):
    #changes value in dict if used in word
    for e in Word:
        if e in Hand:
            Hand[e] -= 1
    #removes key from dict if value is 0
    for key, value in list(Hand.items()):
        if value == 0:
            del Hand[key]
    return Hand


# tests if your created word is actually a word
def Valid(Word, Hand, wordlist):
    #create temporary hand that can be modified w/o side effects
    import copy
    TempHand = copy.deepcopy(Hand)

    #outer loop checks if word is real, inner checks if letters are in hand
    if Word in wordlist:
        for e in Word:
            if e not in TempHand:
                print('no e in word')
                return False
        UpdateHand(TempHand, Word)
        return True
    else:
        return False


def Len(Hand):
    handlen = 0
    for v in Hand.values():
        handlen += v
    return handlen


# play a hand!
def Play(Hand, wordlist):
    load_words()
    TotalScore = 0
    Deal(HandSize)
    Handsize = Len(Hand)
    DispHand(Hand)
    while bool(Hand):
        Word = input('Enter a word using your letters. End game by entering . : ')
        if Word == '.':
            print('Your Score for this hand: ', TotalScore)
            return TotalScore
        else:  
            if Valid(Word, Hand, wordlist) is False:
                print('Word invalid.')
                Score = 0
            else:
                Score = Scoring(Word, Handsize)
                UpdateHand(Hand, Word)
        TotalScore += Score
        DispHand(Hand)
        print('Your total Score is: ', TotalScore)
    print('Hand over.')


HandSize = int(input('How many letters would you like to play with? '))
Hand = Deal(HandSize)

Play(Hand, wordlist)


