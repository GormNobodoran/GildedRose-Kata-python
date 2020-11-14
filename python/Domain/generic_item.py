# -*- coding: utf-8 -*-
from Domain.item import Item


class GenericItem(Item):
    def update(self) -> None:
        if self.isAboveMinQuality():
            self.decreaseQuality()

        if self.isBelowSellInMin() and self.isAboveMinQuality():
            self.decreaseQuality()