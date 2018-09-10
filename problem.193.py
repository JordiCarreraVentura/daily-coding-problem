# This problem was asked by Affirm.
# 
# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock. You're also given a number fee that represents a transaction fee for each buy and sell transaction.
# 
# You must buy before you can sell the stock, but you can make as many transactions as you like.
# 
# For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two (NOTE: ??? we did 4 transactions, 2 purchases and 2 sales. Apparently only e.g. sales are transactions.) transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.

import random

FEE = 2

def f(stocks, pruning=20, verbose=False):
    
    def profit(h):
        if len(h) < 2:
            return 0
        space = [x for x in h]
        p = 0
        while space:
            action, i, value = space.pop(0)
            if action:
                p -= value
            else:
                p += (value - FEE)
        return p
    
    def prune(hh, pruning):
        return sorted(
            hh,
            reverse=True,
            key=lambda x: profit(x)
        )[:pruning]


    def show(ranked):
        for h in ranked:
            print profit(h), h
        print '---'
    
    #   False = sell
    #   True = buy
    
    hh = []
    space = [x for x in enumerate(stocks)]
    for j, stock in space:
        h = [(True, j, stock)]
        hh.append(h)
    
    while space:
        j, stock = space.pop(0)
        _hh = []
        for h in hh:
            bought, k, prev = h[-1]
            if k > j:
                _hh.append(h)
                continue
            if stock - prev > FEE and bought:
                _h = [y for y in h] + [(False, j, stock)]
                _hh.append(_h)
            elif prev - stock > FEE and not bought:
                _h = [y for y in h] + [(True, j, stock)]
                _hh.append(_h)
            _hh.append(h)
        hh = _hh
        if pruning:
            hh = prune(hh, pruning)

    ranked = sorted(
        [h for h in hh if not h[-1][0]],
        reverse=True,
        key=lambda x: profit(x)
    )
    
    if not ranked:
        return 0
    
    if verbose:
        show(ranked)

    return profit(ranked[0])


if __name__ == '__main__':
    
    stocks = [
        [1, 3, 2, 8, 4, 10]
    ] + [
        [   random.randrange(1, 15) if random.random() > 0.8
            else random.randrange(3, 7)
          for i in range(365)
        ] for i in range(19)
    ]
    
    for test in stocks:
        print test
        #profit = f(test, verbose=True)
        profit = f(test)
        print profit
        print
