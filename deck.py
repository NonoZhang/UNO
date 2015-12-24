#!/usr/bin/python
# -*- coding:utf-8 -*-

from cards import *
import copy
import random

class Deck(object):
    def __init__(self, deck):
        self.deck = deck

    def generateCard(self):
        for color in range(0, 4):
            for number in range(0, 15):
                card_number = CardFactory.create_card(number)
                card_color = CardFactory.color(color)
                cards = card_number, card_color
                self.deck.append(cards)
                self.deck.append(copy.deepcopy(cards))
                # print self.deck[color*number+number]

    def shuffle(self):
        for i in range(1, 2*len(self.deck)):
            number = random.randrange(0, len(self.deck))
            temp = self.deck[number]
            self.deck[number] = self.deck[0]
            self.deck[0] = temp
            print self.deck

class CardFactory:
    @staticmethod
    def color(rank):
        if rank == 0:
            color = "red"
        elif rank == 1:
            color = "green"
        elif rank == 2:
            color = "blue"
        elif rank == 3:
            color = "yellow"
        return color

    @staticmethod
    def create_card(rank):
        if rank == 0:
            return ZeroCard("0")
        elif 1<= rank <10:
            return NumberCard(rank)
        elif rank == 10:
            return FourTimesCard("+4")
        elif rank == 11:
            return DoubleCard("+2")
        elif rank == 12:
            return RCard("R")
        elif rank == 13:
            return BanCard("ban")
        elif rank == 14:
            return exChangeCard("change_color")
        else:
            raise Exception("there is something wrong!")