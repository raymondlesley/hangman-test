'''
Created on 20 Dec 2013

@author: L14202
'''

from player import Player

class Game(object):
    '''
    classdocs
    '''


    def __init__(self, player1, player2):
        '''
        Constructor
        '''
        self._player1 = player1
        self._player2 = player2
        self._player1.set_opponent(player2)
        self._player2.set_opponent(player1)

    def word_to_list(self, word):
        letters = []
        for letter in word :
            letters.append(letter)
        return letters

    def play_word(self, p1, p2):
        p1.choose_word()
        guessed = False
        done = False
        misses = 0
        while not done:
            guessed = p2.guess()
            if guessed :
                print("Well done!")
                if p1.all_guessed() :
                    done = True
            else :
                print("Bad luck")
                misses += 1
            print("")
        print("Congratulations")
        input("press <enter>")
        return misses

    def play(self):
        p2misses = self.play_word(self._player1, self._player2)
        p1misses = self.play_word(self._player2, self._player1)
        print(self._player1._name + " missed {0} times".format(p1misses))
        print(self._player2._name + " missed {0} times".format(p2misses))
        if p2misses > p1misses :
            print(self._player1._name + " WINS!")
        elif p1misses > p2misses :
            print(self._player2._name + " WINS!")
        else :
            print("It's a DRAW!")
        input("press <enter>")
