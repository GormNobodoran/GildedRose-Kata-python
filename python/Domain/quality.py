# -*- coding: utf-8 -*-

class Quality:
    __INCREASING_FACTOR = 1
    __DECREASING_FACTOR = 1
    __MIN_QUALITY = 0
    __MAX_QUALITY = 50

    def __init__(self, quality):
        self.quality = quality

    def increase(self) -> None:
        if self.quality < self.__MAX_QUALITY:
            self.quality = self.quality + self.__INCREASING_FACTOR

    def decrease(self) -> None:
        if self.quality > self.__MIN_QUALITY:
            self.quality = self.quality - self.__DECREASING_FACTOR

    def setQualityToMinimum(self) -> None:
        self.quality = self.__MIN_QUALITY
