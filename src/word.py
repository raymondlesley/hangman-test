'''
Created on 20 Dec 2013

@author: L14202
'''

class Word(object):
    '''
    classdocs
    '''


    def __init__(self, word):
        '''
        Constructor
        '''
        self._word = word
        self._letters = []
        self._guesses = []
        self._to_guess = len(word)
        for letter in word :
            self._letters.append(letter)
            self._guesses.append('_')
    
    def guess(self, guess):
        guessed = False
        idx = 0
        for letter in self._letters :
            if (guess.lower() == letter.lower()) :
                guessed = True
                if self._guesses[idx] != letter :
                    self._guesses[idx] = letter
                    self._to_guess -= 1
            idx += 1  # next letter
        return guessed

    def all_guessed(self):
        return self._to_guess == 0

    def guessed_for_display(self):
        display=""
        for letter in self._guesses :
            display += letter + " "
        return display 