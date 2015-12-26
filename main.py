#!/usr/bin/python
# -*- coding:utf-8 -*-

from player import *
from deck import *


if __name__ == '__main__':
    deck = Deck([])
    deck.generateCard()
    print len(deck.deck)
    deck.shuffle()


    playersNumber = 7
    players = []
    for i in range(0, playersNumber):
        players.append(Player("player"+str(i)))
        players[i].init_get_cards(deck.deck, playersNumber)

    for i in range(0, playersNumber):
        players[i].pre_player = players[(i-1) % playersNumber]
        players[i].next_player = players[(i+1) % playersNumber]
        print players[i].name, players[i].pre_player.name, players[i].next_player.name

    print len(deck.deck)















