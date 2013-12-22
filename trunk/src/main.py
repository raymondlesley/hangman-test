'''
Created on 20 Dec 2013

@author: L14202
'''

from game import Game
from player import Player

if __name__ == '__main__':
    pass

print("Let's play Hangman ...")

name = input("Enter a name for player 1 : ")
p1 = Player(name)

name = input("Enter a name for player 2 : ")
p2 = Player(name)


game = Game(p1, p2)
game.play()