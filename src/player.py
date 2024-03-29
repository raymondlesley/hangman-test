'''
Created on 20 Dec 2013

@author: L14202
'''
from word import Word

class Player(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self._name = name
        self._opponent = None
        self._word = None
        self._misses = []

    def set_opponent(self,opponent):
        self._opponent = opponent
        
    def choose_word(self):
        done = False
        while (not done):
            word = input(self._name + ", enter a word : ")
            if (len(word) > 0):
                self._word = Word(word)
                done = True
            else:
                print("A word must have letters!")
        # scroll our word off the screen!
        for i in range(1, 30) : print("")

    def guess_letter(self, letter):
        return self._word.guess(letter)

    def guessed_letters(self):
        return self._word.guessed_for_display()

    def all_guessed(self):
        return self._word.all_guessed()

    def guess(self):
        guessed = self._opponent.guessed_letters()
        print("----------------------------------------------------")
        print("Word : " + guessed)
        print("Incorrect guesses : ", end='')
        print(self._misses)
        done = False
        while (not done):
            letter = input(self._name + ", enter a letter : ")
            done = len(letter) == 1
        guessed = self._opponent.guess_letter(letter)
        if not guessed :
            self._misses.append(letter)
        return guessed