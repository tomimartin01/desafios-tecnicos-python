"""
You are given an integer array coins representing coins of different denominations and an 
integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

>>> change(coins=[1,2,5], amount=11)
3

>>> change(coins=[1,2,5], amount=20)
4

>>> change(coins=[2], amount=3)
-1

>>> change(coins=[1], amount=0)
0

>>> change(coins=[1], amount=1)
1

>>> change(coins=[1], amount=2)
2
""" 

def change(coins, amount):
    
    sum, count  = 0, 0

    for coin in coins[::-1]:
        if sum  < amount:
            div = (amount - sum) //coin 
            sum += coin*div
            count = count + div

    if sum == amount:
        return count

    return -1
        
print(change(coins=[2], amount=3))