#!/usr/bin/python
# -*- coding:utf-8 -*

import random


class Player(object):
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.pre_player = Player
        self.next_player = Player
        self.current_play_card = None
        self.have_play = False
        self.color = None

    def init_get_cards(self, deck, players_number):
        for i in range(0, players_number):
            self.cards.append(deck.deck.pop(0))

    def play_card(self, deck):
        if self.pre_player.current_play_card == None:
            self.current_play_card = random.choice(self.cards)
        else:
            card = self.pre_player.current_play_card
            if(card.property_letter == "+2"):
                tempcard_1= self.find_card_by_letter("+2")
                tempcard_2 = self.find_card_by_letter("+4")
                if tempcard_1 != None :
                    self.current_play_card = tempcard_1
                elif tempcard_2 != None:
                    self.current_play_card = tempcard_2
                else:
                    self.get_card(deck, 2)
            elif(card.property_letter == "+4"):
                tempcard_3 = self.find_card_by_letter("+4")
                if tempcard_3 != None :
                    self.current_play_card = tempcard_3
                else:
                    self.get_card(deck, 4)
            elif(card.property_letter == "ban"):
                self.current_play_card = None
            elif(card.property_letter == "change_color"):
                self.color = random.choice(deck.color)
            else:
                tempcard_4 = self.find_card_by_letter(card.property_letter)
                tempcard_5 = self.find_card_by_color(card.color)
                if(tempcard_4 != None):
                    self.current_play_card = tempcard_4
                elif(tempcard_5 != None):
                    self.current_play_card = tempcard_5
                else:
                    self.get_card(deck, 1)
        if(self.current_play_card != None):
            self.cards.remove(self.current_play_card)
            self.have_play = True
            print self.current_play_card.color, self.current_play_card.property_letter
        else:
            self.have_play = False
            print "***********************"

    def find_card_by_letter(self,letter):

        for temp in self.cards:
            if(temp.property_letter == letter):
                return temp

    def find_card_by_color(self, color):
        for temp in self.cards:
            if(temp.color == color):
                return temp

    def get_card(self, deck, number):
        for i in range(number):
            self.cards.append(deck.deck.pop(0))
            # print deck.deck



