#duelinglist.py
#Justin Hensley
#CSD 1510
#3/16/25
import random
random.seed()
player1 = 0
player2 = 0
p1_list = []
p2_list = []
#User prompt for battles.
battles = int(input("How many battles? "))
#For loop through battles.
for i in range(battles):
    p1 = random.randint(1,50)
    p2 = random.randint(1,50)
    p1_list.append(str(p1))
    p2_list.append(str(p2))
    #Figures the winner of battles.
    if p1 > p2:
        player1 += 1
    else:
        player2 += 1
#Join list like food.py.
player1_join = ", ".join(p1_list)
player2_join = ", ".join(p2_list)

print(f"Player One results: {player1_join}")
print(f"Player Two results: {player2_join}")

print(f"Player One won: {player1}")
print(f"Player Two won: {player2}")
#Find player 1 index and highest score.
largest_p1 = max([int(x) for x in p1_list])
p1_dex = [int(x) for x in p1_list].index(largest_p1)
print(f"Player One best score: {largest_p1} and it is in position: {p1_dex}")
#Find player 2 index and highest score.
largest_p2 = max([int(x) for x in p2_list])
p2_dex = [int(x) for x in p2_list].index(largest_p2)
print(f"Player Two best score: {largest_p2} and it is in position: {p2_dex}")
#Find player 1 index and lowest score.
smallest_p1 = min([int(x) for x in p1_list])
p1_dex = [int(x) for x in p1_list].index(smallest_p1)
print(f"Player One worst score: {smallest_p1} and it is in position: {p1_dex}")
#Find player 2 index and lowest score.
smallest_p2 = min([int(x) for x in p2_list])
p2_dex = [int(x) for x in p2_list].index(smallest_p2)
print(f"Player Two worst score: {smallest_p2} and it is in position: {p2_dex}")
