# -*- coding: utf-8 -*-
from Domain.item import Item


class AgedBrie(Item):
    def update(self) -> None:
        self.decreaseQuality()
        self.decreaseSellIn()

        if self.isBelowSellInMin():
            self.increaseQuality()
