# -*- coding: utf-8 -*-
from Domain.item import Item


class BackstagePass(Item):
    def update(self):
        if self.isBelowMaxQuality():
            self.increaseQuality()

        if self.isBelowSellInMax() and self.isBelowMaxQuality():
            self.increaseQuality()

        if self.isBelowSellInMid() and self.isBelowMaxQuality():
            self.increaseQuality()

        self.decreaseSellIn()

        if self.isBelowSellInMin():
            self.setQualityToMinimum()
