# given that coins are in form of array 
# sorted array [1,1,2,3,5,7,22]
# 


def Solution1(coins):
    coins = coins.sort()

    CoinChangeNeeded = 0
    for coin in coins:
        if coin > CoinChangeNeeded + 1:
            return CoinChangeNeeded + 1
        
        CoinChangeNeeded += coin
    
    return CoinChangeNeeded + 1

coins = [5,7,1,1,2,3,22]