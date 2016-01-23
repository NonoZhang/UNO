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

    def get_available_player(self, player):
        try:
            if player.current_play_card is not None:
                return player
            else:
                return self.get_available_player(player.pre_player)
        except Exception, e:
            print e, "++++cxception++++++"

    def init_get_cards(self, deck, players_number):
        for i in range(0, players_number):
            self.cards.append(deck.deck.pop(0))
            # print "++++++++++++, every get 7 cards from deck", len(deck.deck)

    def find_card(self, deck):
        if self.pre_player.current_play_card is None:
            if self.pre_player.have_play is False:
                player_cu = self.get_available_player(self)
                if player_cu is not None:
                    # print player_cu.current_play_card.color, player_cu.current_play_card.property_letter
                    print " check card pre and pre" + player_cu.name
                    self.play_card_by_logic(player_cu.current_play_card, deck)
                else:
                    self.current_play_card = random.choice(self.cards)
        else:
            self.play_card_by_logic(self.pre_player.current_play_card, deck)

        if self.current_play_card is not None:
            self.cards.remove(self.current_play_card)
            self.have_play = True
            print self.name, self.current_play_card.color, self.current_play_card.property_letter
        else:
            self.have_play = False

    def play_card_by_logic(self, card, deck):
            if card.property_letter == "+2":
                temp_card_1 = self.find_card_by_letter("+2")
                temp_card_2 = self.find_card_by_letter("+4")
                if temp_card_1 is not None:
                    self.current_play_card = temp_card_1
                elif temp_card_2 is not None:
                    self.current_play_card = temp_card_2
                else:
                    self.get_card(deck, self.number_of_double_card(self.pre_player))
                    self.current_play_card = None
            elif card.property_letter == "+4":
                temp_card_3 = self.find_card_by_letter("+4")
                if temp_card_3 is not None:
                    self.current_play_card = temp_card_3
                else:
                    self.get_card(deck, self.number_of_four_card(self.pre_player))
                    self.current_play_card = None
            elif card.property_letter == "ban":
                self.current_play_card.color = card.color
            elif card.property_letter == "change_color":
                self.color = random.choice(deck.color)
                self.current_play_card = card
                self.current_play_card = None
                print "---------change_color-----"
                pass
            else:
                temp_card_4 = self.find_card_by_letter(card.property_letter)
                temp_card_5 = self.find_card_by_color(card.color)
                if temp_card_5 is not None:
                    self.current_play_card = temp_card_5
                elif temp_card_4 is not None:
                    self.current_play_card = temp_card_4
                else:
                    self.get_card(deck, 1)
                    self.current_play_card = None


    def number_of_double_card(self, player):
        try:
            global number
            number = 0
            if player.current_play_card.property_letter == "+2":
                print player.name, player.current_play_card.property_letter
                self.number_of_double_card(player.pre_player)
                number=number +1
                # print number*2, "＋２我需要摸："+str(number*2)+ "张牌"
                return number*2
            else:
                return number*2
        except Exception, e:
            print e, "++++cxception++++++"

    def number_of_four_card(self, player):
        try:
            global number, need_card
            number, need_card = 0, 0
            if player.current_play_card.property_letter == "+4":
                self.number_of_four_card(player.pre_player)
                tmp = 0
                tmp = tmp+1
                need_card = tmp*4 +need_card
                # print need_card, "我一共需要摸："+str(need_card)+"张牌"
                return need_card
            else:
                self.number_of_double_card(player)
                need_card = number *2
                return need_card
        except Exception, e:
            print e, "++++cxception++++++"

    def find_card_by_letter(self, letter):

        for temp in self.cards:
            if temp.property_letter == letter:
                return temp

    def find_card_by_color(self, color):
        for temp in self.cards:
            if temp.color == color:
                return temp

    def get_card(self, deck, number):
        for i in range(number):
            self.cards.append(deck.deck.pop(0))
        print self.name + 'speak: I have get ' + str(number)+' cards from deck'



