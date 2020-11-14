# -*- coding: utf-8 -*-
from Domain.item import Item

class GildedRose(object):
    __HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
    __BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    __AGED_BRIE = "Aged Brie"

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()

