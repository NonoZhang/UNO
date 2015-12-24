#!/usr/bin/python
# -*- coding:utf-8 -*-

from deck import *

class Player(object):
    def __init__(self):
        self.deck = []

    def play_cards(self):
        # self.cards.delete
        pass


    def get_cards(self,cards):
        pass

class NumberCard(object):
    def __init__(self,number):
        self.number = number

class RCard(object):
    def __init__(self,number):
        self.number = number


class BanCard(object):
    def __init__(self, number):
        self.number = number

class ZeroCard(object):
    def __init__(self, number):
        self.number = number

    def exchange(self):
        pass


class DoubleCard:
    def __init__(self,number):
        self.number = number


class FourTimesCard:
    def __init__(self,number):
        self.number = number

class exChangeCard:
    def __init__(self,number):
        self.number = number

if __name__ == '__main__':
    cardFactory = CardFactory()
    deck = Deck([])
    deck.generateCard()
    deck.shuffle()

    players = []
    for i in range(0, 7):
        players.append(Player())












