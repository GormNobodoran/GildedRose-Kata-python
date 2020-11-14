# -*- coding: utf-8 -*-
from Domain.item import Item
from Domain.aged_brie import AgedBrie
from Domain.backstage_pass import BackstagePass
from Domain.hand_of_ragnaros import HandOfRagnaros
from Domain.generic_item import GenericItem


HAND_OF_RAGNAROS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class ItemMaker:

    @staticmethod
    def makeItem(name, sell_in, quality):
        if name == AGED_BRIE:
            return AgedBrie(name, sell_in, quality)

        if name == HAND_OF_RAGNAROS:
            return HandOfRagnaros(name, sell_in, quality)

        if name == BACKSTAGE_PASSES:
            return BackstagePass(name, sell_in, quality)

        return GenericItem(name, sell_in, quality)
