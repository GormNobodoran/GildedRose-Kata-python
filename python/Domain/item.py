# -*- coding: utf-8 -*-
from abc import ABCMeta


class Item(metaclass=ABCMeta):
    __INCREASING_FACTOR = 1
    __DECREASING_FACTOR = 1
    __MIN_QUALITY = 0
    __MAX_QUALITY = 50

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def increaseQuality(self) -> None:
        self.quality = self.quality + self.__INCREASING_FACTOR

    def decreaseQuality(self) -> None:
        self.quality = self.quality - self.__DECREASING_FACTOR

    def isAboveMinQuality(self) -> bool:
        return self.quality > self.__MIN_QUALITY

    def isBelowMaxQuality(self) -> bool:
        return self.quality < self.__MAX_QUALITY
