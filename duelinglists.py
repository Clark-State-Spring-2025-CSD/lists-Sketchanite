#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

player_one_numbers = []
player_two_numbers = []

for i in range(10):
    player_one_numbers.append(random.randint(1, 50))
    player_two_numbers.append(random.randint(1, 50))

player_one_win_count = 0
player_two_win_count = 0

for i in range(10):
    num_one = player_one_numbers[i]
    num_two = player_two_numbers[i]
    
    if num_one > num_two:
        player_one_win_count += 1
    elif num_two > num_one:
        player_two_win_count += 1

highest_player_one = player_one_numbers[0]
highest_player_one_index = 0
lowest_player_one = player_one_numbers[0]
lowest_player_one_index = 0

for i in range(1, 10):
    if player_one_numbers[i] > highest_player_one:
        highest_player_one = player_one_numbers[i]
        highest_player_one_index = i
    if player_one_numbers[i] < lowest_player_one:
        lowest_player_one = player_one_numbers[i]
        lowest_player_one_index = i

highest_player_two = player_two_numbers[0]
highest_player_two_index = 0
lowest_player_two = player_two_numbers[0]
lowest_player_two_index = 0

for i in range(1, 10):
    if player_two_numbers[i] > highest_player_two:
        highest_player_two = player_two_numbers[i]
        highest_player_two_index = i
    if player_two_numbers[i] < lowest_player_two:
        lowest_player_two = player_two_numbers[i]
        lowest_player_two_index = i

print("Player One =", player_one_numbers)
print("Player Two =", player_two_numbers)

print(f"Player one won {player_one_win_count} times")
print(f"Player two won {player_two_win_count} times")

print(f"Player one's highest number is {highest_player_one} at index {highest_player_one_index}")
print(f"Player two's highest number is {highest_player_two} at index {highest_player_two_index}")

print(f"Player one's lowest number is {lowest_player_one} at index {lowest_player_one_index}")
print(f"Player two's lowest number is {lowest_player_two} at index {lowest_player_two_index}")
