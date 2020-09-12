# Arnaud Legoux Moving Average (ALMA) in Python

This is a small Technical Analysis library for the calculation of Arnaud Legoux Moving Average (ALMA). It is built in Pandas and Numpy and uses [TA](https://github.com/bukosabino/ta).

## Description

The Arnaud Legoux Moving Average (ALMA) indicator is a superior moving average as compared to the Exponential Moving and Simple Moving Averages. Arnaud Legoux and Dimitrios Kouzis Loukas developed the indicator in the year 2009. The objective of ALMA is to minimize the noise and produce a more reliable signal than the conventional moving averages. The indicator (ALMA) removes small price fluctuations and also enhances the trend by applying a moving average (MA) twice, once from left to right, and once from right to left.

## Key Points on ALMA Indicator

- ALMA indicator works on the principle of the Moving Average (MA), but the calculation formula is more perfect.
- The main difference in regards to conventional moving averages is its minimal lag.
- The classic EMA, SMA, SMMA and other Moving Average lines have a significant minus – signal lag.
- The MA ALMA in this regard is more perfect. In a volatile market, this tool shows very good trading results, even without the use of auxiliary filters.

The Arnaud Legoux moving average attempts to bridge the gap and thus is expected to show both responsiveness and smoothness at the same time. Generally, the Arnaud Legoux Moving Average indicator applies the moving average twice, once from left to right and the other from right from left with the process said to eliminate price lag or phase shift significantly, a problem that is common to the traditional moving averages.

Source: Read more on [Stock Maniacs](https://www.stockmaniacs.net/arnaud-legoux-moving-average-indicator/)

## How to Use

```python
# import the package
from AlmaIndicator import ALMAIndicator

# define a Pandas dataframe which should contain closing price of the stocks
df = ...

# initialize the indicator
# you only need to provide a Pandas series of the closing price of the stock
alma_indicator = ALMAIndicator(close=df['close'])
# add alma to dataframe by calling the alma function
df['alma'] = alma_indicator.alma()
```

## Sample Result

![spy - data](https://user-images.githubusercontent.com/29625844/92999031-54f8c600-f550-11ea-974c-ae96fdb8e623.png)

Note that there will be `NaN` values at the beginning of the ALMA series since there is a window of analysis which is set to 9. In other words, your dataset must at least contain 9 entries.

## Sample Figure

![spy - alma](https://user-images.githubusercontent.com/29625844/92998867-1d3d4e80-f54f-11ea-919c-dd48c8927172.png)
