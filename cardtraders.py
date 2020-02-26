#import function randint directly from random package
from random import randint

#Generate Bob's and Alice's starting cards
#[randint(1, 9) for i in range(13)] generates a list of 13 random ints,
#from 1 to 9
#the for j in range(2) does it twice, creating a tuple of
#2 lists to unpack into variables Bob and Alice
Bob, Alice = ([randint(1, 9) for i in range(13)] for j in range(2))
#print the starting cards
print(f"Bob starts with {Bob}")
print(f"Alice starts with {Alice}")
