# -*- coding: utf-8 -*-
from Domain.item import Item


class GenericItem(Item):
    def update(self) -> None:
        self.decreaseQuality()

        if self.isBelowSellInMin():
            self.decreaseQuality()
