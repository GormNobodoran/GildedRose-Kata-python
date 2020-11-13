# -*- coding: utf-8 -*-
from Domain.item import Item


class AgedBrie(Item):
    def update(self) -> None:
        if self.isBelowMaxQuality():
            self.decreaseQuality()

        self.decreaseSellIn()

        if self.isBelowSellInMin() and self.isBelowMaxQuality():
            self.increaseQuality()
