#!/usr/bin/python
# -*- coding:utf-8 -*-

from cards import *
import copy
import random

class Deck(object):
    def __init__(self, deck):
        self.deck = deck
        self.color = ["green", "yellow", "red", "blue"]
        self.letter = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+2", "+4", "ban", "revers", "change_color"]

    def generateCard(self):
        for color in self.color:
            for letter in self.letter:
                cards = Card(color, letter)
                self.deck.append(cards)
                self.deck.append(copy.deepcopy(cards))
                # print cards.color, cards.propertyLetter

    def shuffle(self):
        for i in range(1, 2*len(self.deck)):
            number = random.randrange(0, len(self.deck))
            temp = self.deck[number]
            self.deck[number] = self.deck[0]
            self.deck[0] = temp
