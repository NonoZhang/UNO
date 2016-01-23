#!/usr/bin/python
# -*- coding:utf-8 -*-

from player import *
from deck import *


if __name__ == '__main__':
    deck = Deck()
    deck.generate_card()
    # print len(deck.deck)
    deck.shuffle()
    players_number = 7
    players = []
    for i in range(0, players_number):
        players.append(Player("player"+str(i)))
        players[i].init_get_cards(deck, players_number)

    for i in range(0, players_number):
        players[i].pre_player = players[(i-1) % players_number]
        players[i].next_player = players[(i+1) % players_number]
        # print players[i].name, players[i].pre_player.name, players[i].next_player.name

    flag = True
    while len(deck.deck) > 0 and flag:
        for i in range(0, players_number):
            # print players[i].name
            players[i].find_card(deck)
            # print len(deck.deck)
            if len(players[i].cards) == 0:
                print "is over "
                flag = False
                break

    #
    # for i in range(0, players_number):
    #         players[i].play_card(deck)
    # for i in range(0, players_number):
    #         players[i].play_card(deck)










