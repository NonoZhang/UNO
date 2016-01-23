#!/usr/bin/python
# -*- coding:utf-8 -*-


class Card(object):
    def __init__(self, property_letter, color):
        self.property_letter = property_letter
        self.color = color
    # def __str__(self):
    #     return " property_letter = " + self.property_letter , " color = " + self.color
    # def __repr__(self):
    #     print " property_letter = " + self.property_letter , " color = " + self.color