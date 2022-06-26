# TASK 1
# QUESTION 1

# rain = input("Is it raining today? y/n")
# if rain == "y":
#     print("Take an umbrella")
# else:
#     print("You don't need an umbrella")

# QUESTION 2
#
# my_money = input('How much money do you have? ')
# boat_cost = 20 + 5
# if int(my_money) > boat_cost:
#     print('You can afford the boat hire')
# else :
#     print('You cannot afford the board hire')

# QUESTION 3
#
# import math
# year=input("When was this book published")
#
#
# year_century= int(str(year)[:2])
# century = int(year_century) + 1
#
# year_decade = int(str(year)[-2:])
# decade = math.floor(int(str(year_decade))/10)*10
#
# print("{} century, {}th".format(century,decade))


# TASK 2

# QUESTION 1


# The reason the programme is not showing the first item on the list, is because in the last line:
# print(shopping_list[1])
# the chosen number is 1 and while in Python we start counting with 0, which will print the second item. In order to print the first item, we need to write:
# print(shopping_list[0])

# QUESTION 2
#
# chocolates = {'white': 1.50, 'milk': 1.20, 'dark': 1.80, 'vegan': 2.00 }
#
# item = input("Which chocolate would you like to buy?")
# if item == "white" :
#    print("It is {}".format(chocolates["white"]))
# elif item == "mik" :
#    print("It is {}".format(chocolates["milk"]))
# elif item == "dark" :
#    print("It is {}".format(chocolates["dark"]))
# elif item == "vegan" :
#    print("It is {}".format(chocolates["vegan"]))
# else :
#    print("We do not sell this chocolate")

# QUESTION 3
#
# import random
#
# lotteryNumbers = []
#
# for i in range (0,7):
#     number = random.randint(1,100)
#
#     while number in lotteryNumbers:
#         number = random.randint(1,100)
#     lotteryNumbers.append(number)
#
# userNumbers = []
# for i in range (0,7):
#     number = int(input("Please enter a number between 1 and 100"))
#     while (number in userNumbers or number<1 or number>100):
#         print("Invalid number, please try again")
#         number = int(input("Please enter a number between 1 and 100"))
#     userNumbers.append(number)
#
# counter = 0
# for number in userNumbers:
#     if number in lotteryNumbers:
#         counter +=1
#         if counter == 3:
#             print("You have three matching numbers and you win £20!")
#         elif counter == 4:
#             print("You have four matching numbers and you win £40!")
#         elif counter == 5:
#             print("You have five matching numbers and you win £100!")
#         elif counter == 6:
#             print("You have six matching numbers and you win £10000!")
#         elif counter == 7:
#             print("You have seven matching numbers and you win £1000000!")
#
#
# print("Today's lottery numbers are: {} ".format(lotteryNumbers))
# print("Your number selection is: {} ".format(userNumbers))

# TASK 3
#
# QUESTION 1
#
# Pip is a package manager for Python which allows us to install additional libraries and packages which are not a part of the standard Python library.
# It is extremally easy to instal and gives the opportunity to use libraries which allows us to finish the code much quicker as we do not need to write every code from the scratch because someone else have already wrote it.
# For example, there is a module NUMPY which contains multidimensional arrays and matrix data structures. It gives us many more opportunities to work with the data in an easy way without coding the logic behind it.


# QUESTION 2
#
# poem='I like Python and I am not good at poems'
# with open('song.txt', 'w+') as poem_file:
#    poem_file.write(poem)

# QUESTION 3
#
# song_file = open("song.txt" , "w")
#
# song_file.write("""You could never know what it's like.\n
#             Your blood like winter freezes just like ice.\n
#             And there's a cold lonely light that shines from you\n
#             You'll wind up like the wreck you hide behind that mask you use\n
#             And did you think this fool could never win?\n
#             Well look at me, I'm coming back again\n
#             I got a taste of love in a simple way\n
#             And if you need to know while I'm still standing, you just fade away\n
#             Don't you know I'm still standing better than I ever did\n
#             Looking like a true survivor, feeling like a little kid\n
#             I'm still standing after all this time\n
#             Picking up the pieces of my life without you on my mind\n
#             I'm still standing (Yeah, yeah, yeah)\n
#             I'm still standing (Yeah, yeah, yeah")"""


# QUESTION 2

# The file has been created successfully.

# QUESTION 3
#
# stillSong = []
# with open('song.txt', 'rt') as s:
#    data = s.readlines()
# for line in data:
#    if "still" in line:
#       print(line)
#       stillSong.append(line)
# print(stillSong)

# TASK 4
#
# import requests
# from pprint import pprint as pp
# #pokemon_number = input("What is the Pokemon's ID? ")
# pokemon_ids_list = [1,2,3,4,5,6]
#
# url = 'https://pokeapi.co/api/v2/pokemon/'
#
# for i in pokemon_ids_list:
#     request = url+str(i)
#     response = requests.get(request)
#     data = response.json()
#     #print(data)
#     name = data['name']
#     moves = data['moves']
#     print(f'Name: {name}')
#     print('Moves:')
#     for move in moves:
#         print('\t' + move['move']['name'])
