#!/usr/bin/python
# -*- coding:utf-8 -*
from cards import *

class Player(object):

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.pre_players = object
        self.next_players = object
        self.current_playcard = None

    def init_get_cards(self, deck, playersNumber):
        for i in range(0, playersNumber):
            self.cards.append(deck.pop(0))

    def play_card(self):
        pass



