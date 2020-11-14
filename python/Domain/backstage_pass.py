# -*- coding: utf-8 -*-
from Domain.item import Item


class BackstagePass(Item):
    def update(self):
        self.increaseQuality()

        if self.isBelowSellInMax():
            self.increaseQuality()

        if self.isBelowSellInMid():
            self.increaseQuality()

        self.decreaseSellIn()

        if self.isBelowSellInMin():
            self.setQualityToMinimum()
