#!/usr/bin/python
# -*- coding:utf-8 -*-
colors = ['red', 'blue', 'yellow', 'green']
normal_cards = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+2', 'R', 'ban']
no_color = {'+4', 'change_color'}


class Player:
    def __init__(self,cards):

        #init seven cards
        self.cards = []

    def play_cards(self):
        #self.cards.delete


    def get_cards(self,cards):
        pass


class Deck:
    def __init__(self):
        pass



class NumberCard:
    def __init__(self,color,number):
        pass

class RCard:
    def __init__(self,color):
        self.letter="R"
        self.color = color


class BanCard:
    def __init__(self,color):
        self.letter = "ban"

class ExchangeCard:
    def __init__(self,color):
        self.letter="0"

    def exchange(self):
        pass


class NormalCard:
    def __init__(self, color, letter):
        pass


class SpecialCard:
    def __init__(self, letter):
        pass

class CardFactory:
    @staticmethod
    def create_card(self, type):
        if type is "normal":
            return NormalCard(colors, letter)
        if type is "special":
            return SpecialCard(letter)


if __name__ == '__main__':
    card = CardFactory().createCard("normal")
