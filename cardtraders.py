#import function randint directly from random package
#repl: https://cs2019-2020.subwayman.repl.run/
from random import randint
#This solution does not use sets!
#Card range has also been adjusted to 1-14, 1-9 is a bit small
#Even then, situations where no trades can be made are quite common


#Generate Bob's and Alice's starting cards
#[randint(1, 9) for i in range(13)] generates a list of 13 random ints,
#from 1 to 9
#the for j in range(2) does it twice, creating a tuple of
#2 lists to unpack into variables Bob and Alice
Bob, Alice = ([randint(1, 14) for i in range(13)] for j in range(2))
#for more information look up 'list comphrehensions'
#print the starting cards
print(f"Bob starts with {sorted(Bob)}")
print(f"Alice starts with {sorted(Alice)}\n")

#Rules to follow:
#One cannot trade for a card he/she already has
#One cannot trade away cards of which he/she only posesses one
#one cannot trade for nothing
#Eliminate all non-tradeable cards and create new datasets for each
#We want to remember the original cards, so create new variables
#instead of overwriting the old ones
Bob_trades = list(elem for elem in set(Bob) if Bob.count(elem) > 1 and elem not in Alice)
Alice_trades = list(elem for elem in set(Alice) if Alice.count(elem) > 1 and elem not in Bob)
#creates list of cards Bob and Alice are willing to trade away, by
#iterating through their cards and checking if
#they have duplicates or not
#Also ckecks if the other person has the card or not
#Now that we have all possible cards each person can trade,
#we can iterate through and pair them
for _ in range(min(len(Bob_trades), len(Alice_trades))):
    #We iterate the length of the smaller list
    #Take the last two values out of each list and assign them to variables
    #Pop from the end of the list, x.pop(0) is a very slow operation since
    #the index for each value has to change
    x = Bob_trades.pop(-1)
    y = Alice_trades.pop(-1)
    #remove one instance of the traded card from each
    Bob.remove(x)
    Alice.remove(y)
    #complete the trade
    Bob.append(y)
    Alice.append(x)
    #print the trade
    print(f"Bob traded {x} for Alice's {y}")

print("")
#print results
print(f"Bob ends with {sorted(Bob)}")
print(f"Alice ends with {sorted(Alice)}")
