# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from Domain.sell_in import SellIn
from Domain.quality import Quality


class Item(metaclass=ABCMeta):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = SellIn(sell_in)
        self.quality = Quality(quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def increaseQuality(self) -> None:
        self.quality.increase()

    def decreaseQuality(self) -> None:
        self.quality.decrease()

    def setQualityToMinimum(self) -> None:
        self.quality.setQualityToMinimum()

    def decreaseSellIn(self) -> None:
        self.sell_in.decrease()

    def increaseSellIn(self) -> None:
        self.sell_in.increase()

    def isBelowSellInMax(self) -> bool:
        return self.sell_in.isBelowMaxSellIn()

    def isBelowSellInMid(self) -> bool:
        return self.sell_in.isBelowMidSellIn()

    def isBelowSellInMin(self) -> bool:
        return self.sell_in.isBelowMinSellIn()

    @abstractmethod
    def update(self) -> None:
        pass


