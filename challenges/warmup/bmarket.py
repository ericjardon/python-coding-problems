def barterMarket(comicBooks, coins, coinsNeeded, coinsOffered):
    # Return max num of fiction books attainable
    x = coinsNeeded
    y = coinsOffered
    memo={}
    
    def barter(comics, coins, fictionBooks, memo):
        if (comics, coins) not in memo:
            if comics == 0:
                return fictionBooks
            
            if coins >= x:
                purchase = barter(comics-1, coins-x, fictionBooks +1, memo)
                    
                sell = barter(comics-1, coins+y, fictionBooks, memo)
            
                return max(purchase, sell)
            else:
                memo[(comics,coins)] = 0
            
        return memo[(comics,coins)]
                
    return barter(comicBooks, coins, 0, memo)


def barterMarketFaster(comicBooks, coins, coinsNeeded, coinsOffered):
    best = 0
    for sold in range(comicBooks):
        avail_coins = coins + coinsOffered*sold

        if comicBooks >= (avail_coins//coinsNeeded):
            best = max((avail_coins//coinsNeeded), best)
    
    return best
    # Does not beat all test cases