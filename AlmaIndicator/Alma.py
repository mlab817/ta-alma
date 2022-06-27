import numpy as np
import pandas as pd
from math import exp
from ta.utils import IndicatorMixin


class ALMAIndicator(IndicatorMixin):
    def __init__(
            self,
            close: pd.Series,
            fillna: bool = False,
            window: int = 9):
        self._close = close
        self._fillna = fillna
        self._window = window
        self._run()

    def _run(self):
        self._alma_weights = self.alma_weights(window=self._window)
        self._calculate_alma = self.calculate_alma()
        self._alma = self._close.rolling(window=self._window).apply(self.calculate_alma)

    def alma(self) -> pd.Series:
        alma = self._check_fillna(self._alma, value=0)
        return pd.Series(alma, name=f'alma')

    def calculate_alma(self, prices: list = [], window: int = 9):
        """
        Calculates and returns ALMA figure
        """
        weights = self._alma_weights
        if len(prices) < self._window:
            return None
        else:
            weighted_sum = weights * prices
            alma = weighted_sum.sum() / weights.sum()
            return alma

    def alma_weights(self, window=9, offset=0.85, sigma=6):
        """
        Calculates ALMA weights and returns array
        """
        m = int(offset * (window - 1))
        s = (window / sigma)
        k_all = list(range(0, window))
        weights = []
        # this generates a reversed weights
        for k in k_all:
            Wtd = exp(-((k - m) ** 2) / (2 * (s ** 2)))
            weights.append(Wtd)
        return np.array(weights)
