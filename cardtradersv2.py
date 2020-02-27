
from random import randint

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


#Eliminate all non-tradeable cards and create new datasets for each

Bob_trades = set(i for i in Bob if Bob.count(i) > 1) - set(Alice)
Alice_trades = set(i for i in Alice if Alice.count(i) > 1) - set(Bob)

#creates list of cards Bob and Alice are willing to trade away, by
#iterating through their cards and checking if
#they have duplicates or not
#Also checks if the other person has the card or not

#iterate through and pair them
while Bob_trades and Alice_trades:
    #We iterate the length of the smaller list
    #Take the last two values out of each list and assign them to variables
    x = Bob_trades.pop()
    y = Alice_trades.pop()
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
