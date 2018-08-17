#Loops allow you to automate repetitive tasks.
#Read the directions in the exercises below and don't forget to print your results and commit and push your code after each exercise!

#Now, go ahead and get loopy!

#1 Order Up
#Create a for loop that will iterate through 8 numbers starting from 1 and print the following:
for i in (range(1,9)):
    print(f"Number {i}, your order is ready")
#'Number 1, your order is ready.'
#'Number 2, your order is ready.'
# ...
# ...
# ...
##'Number 8, your order is ready.'


#2 Now Serving
#Create a while loop that will print the following message:
for i in range(1,6):
    print(f"Now server number {i}")
#'Now serving number 1.'
#'Now serving number 2.'
# ...
# ...
# ...
# 'Now serving number 5.'


#3 3 is a Magic Number
#Create a while loop that will generate a multiplication table for the number 3 and print out the following:
# 1 x 3 = 3
# 2 x 3 = 6
# 3 x 3 = 9
# 4 x 3 = 12
# ...
# ...
# ...
# 9 x 3 = 27
for i in range(1,10):
    val = i * 3
    print(f'{i} x 3 = {val}')

#4. Uber This!
# Declare a variable named cars and assign it a list of 5 of your favorite car brands. Next create a for loop that will iterate through the cars list and prints the following: 'My next car will be a red x.' Where x represents each item in the list.

cars = ['Lamborghini','Porsche','Ferrari','Bugatti','MacLaren']
for car in cars:
    print(f'My next car will be a red {car}')
#5 Uber This Again
#Print each item in the above cars list using a while loop.
while car in cars:
    if car == 'MacLaren':
        break
    print(f'My next car will be a red {car}')
#6  No More Tears
# Create a for loop that will iterate through the cyber attacks list and prints the following: 
#The attack at 0 is Wannacry.
#The attack at 1 is Petya.
#The attack at 2 is Locky.
#The attack at 3 is Krack Attack
#The attack at 4 is Sambacry.
#DO NOT use numbers in your string.

cyber_attacks = ['Wannacry', 'Petya', 'Locky', 'Krack Attack', 'Sambacry']
for i in range(len(cyber_attacks)):
    print(f'The attack at {i} is {cyber_attacks[i]}')

#7 Even
# Declare a variable named even_list and assign it an empty list. Next, write a for loop that will place 25 even numbers starting from 0 into the even_list list. Print the even_list variable to see your results. 
even_list = []
for i in range(0,51,2):
    even_list.append(i)

print(even_list)


#8 Sum Up
# Create a function named add_up which takes a parameter num. In the code block inside the function, create a variable named sum and assign it a number value of 0. Next, create a for loop that will iterate through a list of numbers using the range function that will be determined by the num parameter and will sum up all the numbers in the list and store it to the sum variable. Print the sum variable to see your results.

#i.e a number list of 10 will have a sum total of 45


#9 East Coast vs West Coast - A Hip Hop Rivalry
#The East Coast - West Coast hip hop rivalry was a feud between artist and fans of the East Coast hip hop and West Coast hip hop scenes from the mid to last 1990s. 

#Your job is to create a function that will loop through the rappers list and place all the odd indexed items in a list named weessst_side and all the even indexed items in a list named east_side. Print your results.

rappers = ['Tupac', 'Biggie', 'Ice Cube', 'Nas', 'Snoop', '50 Cent', 'Nate Dogg', 'Wu Tang Clan', 'Kendrick Lamar']

#10 Breaking Up is Easy
#Create a for loop that will iterate through 10 even numbers (starting from 0) and stop printing at 10.


#11 Zip Codes
#Create a for loop that will iterate through the zip codes list below and print all the zip codes except for 96822.

zip_codes = [90001,90002,90003,90004,90005,96822,90007,90008,90010,90011,90012,90013,90014,90015, 90016,90017,90018,90019]


#12 Fizz Buzz!
#The classic programming task is back! Use a for loop that will iterate through 100 numbers starting from 1. Your job is to program the following:

#  a) if the number is a multiple of 3, it should print 'Fizz'
#  b) if the number is a multiple of 5, it should print 'Buzz'
#  c) if the number is a multiple of 3 and 5, it should print 'Fizz Buzz'
#  d) if the number is neither a multiple of 3 and 5, it should print the number

#example output:
# 1
# 2
# Fizz
# 4
# Buzz
# ...
# ...
# ...
# 14
# Fizz Buzz


#13 Fizz Buzz Again 
#Do the same thing again using a while loop.

