# -*- coding: utf-8 -*-
from Domain.item import Item

class GildedRose(object):
    __HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
    __BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    __AGED_BRIE = "Aged Brie"
    __SELL_IN_LONG = 11
    __SELL_IN_MID = 6
    __SELL_TODAY = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != self.__AGED_BRIE and item.name != self.__BACKSTAGE_PASSES:
                if item.isAboveMinQuality():
                    if item.name != self.__HAND_OF_RAGNAROS:
                        item.decreaseQuality()
            else:
                if item.isBelowMaxQuality():
                    item.increaseQuality()
                    if item.name == self.__BACKSTAGE_PASSES:
                        if item.sell_in < self.__SELL_IN_LONG:
                            if item.isBelowMaxQuality():
                                item.increaseQuality()
                        if item.sell_in < self.__SELL_IN_MID:
                            if item.isBelowMaxQuality():
                                item.increaseQuality()
            if item.name != self.__HAND_OF_RAGNAROS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < self.__SELL_TODAY:
                if item.name != self.__AGED_BRIE:
                    if item.name != self.__BACKSTAGE_PASSES:
                        if item.isAboveMinQuality():
                            if item.name != self.__HAND_OF_RAGNAROS:
                                item.decreaseQuality()
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.isBelowMaxQuality():
                        item.increaseQuality()




