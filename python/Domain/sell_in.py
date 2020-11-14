# -*- coding: utf-8 -*-

class SellIn:
    __DECREASING_FACTOR = 1
    __INCREASING_FACTOR = 1
    __MAX_SELL_IN = 11
    __MID_SELL_IN = 6
    __MIN_SELL_IN = 0

    def __init__(self, sell_in):
        self.sell_in = sell_in

    def increase(self) -> None:
        self.sell_in = self.sell_in + self.__INCREASING_FACTOR

    def decrease(self) -> None:
        self.sell_in = self.sell_in - self.__DECREASING_FACTOR

    def isBelowMaxSellIn(self) -> bool:
        return self.sell_in < self.__MAX_SELL_IN

    def isBelowMidSellIn(self) -> bool:
        return self.sell_in < self.__MID_SELL_IN

    def isBelowMinSellIn(self) -> bool:
        return self.sell_in < self.__MIN_SELL_IN
