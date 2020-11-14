# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    __INCREASING_FACTOR = 1
    __DECREASING_FACTOR = 1
    __MIN_QUALITY = 0
    __MAX_QUALITY = 50
    __SELL_IN_DECREASING_FACTOR = 1
    __SELL_IN_INCREASING_FACTOR = 1
    __SELL_IN_MAX = 11
    __SELL_IN_MID = 6
    __SELL_IN_MIN = 0

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def increaseQuality(self) -> None:
        if self.isBelowMaxQuality():
            self.quality = self.quality + self.__INCREASING_FACTOR

    def decreaseQuality(self) -> None:
        if self.isAboveMinQuality():
            self.quality = self.quality - self.__DECREASING_FACTOR

    def setQualityToMinimum(self) -> None:
        self.quality = self.__MIN_QUALITY

    def isAboveMinQuality(self) -> bool:
        return self.quality > self.__MIN_QUALITY

    def isBelowMaxQuality(self) -> bool:
        return self.quality < self.__MAX_QUALITY

    def decreaseSellIn(self) -> None:
        self.sell_in = self.sell_in - self.__SELL_IN_DECREASING_FACTOR

    def increaseSellIn(self) -> None:
        self.sell_in = self.sell_in + self.__SELL_IN_INCREASING_FACTOR

    def isBelowSellInMax(self) -> bool:
        return self.sell_in < self.__SELL_IN_MAX

    def isBelowSellInMid(self) -> bool:
        return self.sell_in < self.__SELL_IN_MID

    def isBelowSellInMin(self) -> bool:
        return self.sell_in < self.__SELL_IN_MIN

    @abstractmethod
    def update(self) -> None:
        pass


