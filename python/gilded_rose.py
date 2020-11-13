# -*- coding: utf-8 -*-


class GildedRose(object):
    __HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
    __BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    __AGED_BRIE = "Aged Brie"
    __MIN_QUALITY = 0
    __MAX_QUALITY = 50
    __SELL_IN_LONG = 11
    __SELL_IN_MID = 6
    __SELL_TODAY = 0

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != self.__AGED_BRIE and item.name != self.__BACKSTAGE_PASSES:
                if item.quality > self.__MIN_QUALITY:
                    if item.name != self.__HAND_OF_RAGNAROS:
                        item.quality = item.quality - 1
            else:
                if item.quality < self.__MAX_QUALITY:
                    item.quality = item.quality + 1
                    if item.name == self.__BACKSTAGE_PASSES:
                        if item.sell_in < self.__SELL_IN_LONG:
                            if item.quality < self.__MAX_QUALITY:
                                item.quality = item.quality + 1
                        if item.sell_in < self.__SELL_IN_MID:
                            if item.quality < self.__MAX_QUALITY:
                                item.quality = item.quality + 1
            if item.name != self.__HAND_OF_RAGNAROS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < self.__SELL_TODAY:
                if item.name != self.__AGED_BRIE:
                    if item.name != self.__BACKSTAGE_PASSES:
                        if item.quality > self.__MIN_QUALITY:
                            if item.name != self.__HAND_OF_RAGNAROS:
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < self.__MAX_QUALITY:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)