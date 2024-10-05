#1. Write a function which generates a six digit/character random_user_id.

import random
def random_user_id(digits):
    hex_characters = string.hexdigits
    sequence = random.choices(hex_characters, k=digits)
    #so I had to make an empty string to be able to add those ids
    result = ''.join(sequence)
    return result
random_user_id(6)


#2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

def user_input_length(length):
    length_char=input('How many characters should the user ID be?')
    return length
def user_amount_of_ids(amounts):
    amounts=input('How many IDs should we create')
    return amount
def user_id_gen_by_user(user_input_length, user_amount_of_ids):
    hex_characters = string.hexdigits
    sequence = random.choices(hex_characters, k=user_input_length)
    result= ''.join(sequence)
    result_list=[]
    result_list.insert(0, result)
    return result 
user_id_gen_by_user((user_input_length), (user_amount_of_ids))


#i dont think this had to be a function atleast the first two parts

import string
import random
user_input_length=int(input('How many characters should the user ID be?'))
user_amount_of_ids=int(input('How many IDs should we create'))
def user_id_gen_by_user(user_input_length, user_amount_of_ids):
    hex_characters = string.hexdigits
    sequence = random.choices(hex_characters, k=user_input_length)
    result= (''.join(sequence))
    return result 
user_id_gen_by_user((user_input_length), (user_amount_of_ids))
#that gets far as producing one id in google colab, however I need to make 5, maybe I store the result in a list? 
#yes
#but how do i get it to loop like x times 


#lol, i have the return statement inside of the for loop so after the first iteration it cancels 
import string
import random
user_input_length=int(input('How many characters should the user ID be?'))
user_amount_of_ids=int(input('How many IDs should we create'))
result_list=[]
def user_id_gen_by_user(user_input_length, user_amount_of_ids):
  for number in range(user_amount_of_ids):
    hex_characters = string.hexdigits
    sequence = random.choices(hex_characters, k=user_input_length)
    result= ''.join(sequence)
    result_list.append(result)
    number = number - 1
  return result_list
(user_id_gen_by_user((user_input_length), (user_amount_of_ids))

#3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
'''
#define 3 variables
1. red
2. green
3. blue

define the function
the 3 vars are just going to be the random.randrange(0,255) is the step 1 by default like range?

store the output as a string with string formatting display the color
'''
#THIS WORKED FIRST TRY 
import random
def rgb_color_gen():
    red=random.randrange(0,255)
    blue=random.randrange(0,255)
    green=random.randrange(0,255)
    color_string=(red, blue, green)
    return color_string
print(rgb_color_gen())


# EXERCISES LEVEL 2
#homie look how hard this one looks
#1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import random
import string
result_list=[]
def list_of_hexa_colors(amount):
    for i in range(amount):
        hex_characters=string.hexdigits
        sequence=random.choices(hex_characters, k=6)
        result='#'.join(sequence)
        result_list.append(result)
        i = i -1 
# redundant in this code ^ 
    return result_list
print(list_of_hexa_colors(5))

#2 Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

import random
color_list=[]
def list_of_rgb_colors(amount):
    for i in range(amount):
        red=random.randrange(0,255)
        blue=random.randrange(0,255)
        green=random.randrange(0,255)
        color_string=(red, blue, green)
        color_list.append(color_string)
    return color_list
print(list_of_rgb_colors(5))

'''
list_of_hexa_colors 
should be a function that takes argument amount as integer
'''

'''
#given an integer n, return true if its a power of 4 return false if its not 
n=16
if n ** 0.25 != int: 
    print(False)
elif n ** 0.25 == int:
    print(True)
'''
#3. Write a function generate_colors which can generate any number of hexa or rgb colors.

import random
import string
color_list=[]
color_type='hexa' or 'rgb'
#removed ^^^^^^^^^^^^^^^^^
def generate_colors(color_type, amount):
    if color_type == 'hexa':
        for i in range(amount):
            hex_characters=string.hexdigits
            sequence=random.choices(hex_characters, k=6)
            result=''.join(sequence)
            with_hash='#'+result
            color_list.append(with_hash)
    elif color_type == 'rgb':
        for i in range(amount):
            red=random.randrange(0,255)
            blue=random.randrange(0,255)
            green=random.randrange(0,255)
            color_string=(red, blue, green)
            color_list.append(color_string)
    return color_list
print(generate_colors('hexa',7))
print(generate_colors('rgb',7))

#some changes per gpt
#color list gets initialized inside the function so I can reset it after each call; if I didn't want 
# that or statement: Using or in assignment: The line color_type='hexa' or 'rgb' does nothing meaningful. It will always evaluate to 'hexa'. Instead, you should pass the desired value as an argument to the function.

import random
import string

def generate_colors(color_type, amount):
    color_list = []  # Initialize inside the function to avoid persistence between calls
    
    if color_type == 'hexa':
        for _ in range(amount):
            # Generate 6 random hex characters and ensure they are uppercase or lowercase consistently
            sequence = ''.join(random.choices(string.hexdigits[:16], k=6)).upper()
            with_hash = f'#{sequence}'
            color_list.append(with_hash)
    
    elif color_type == 'rgb':
        for _ in range(amount):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            color_list.append((red, green, blue))
    
    return color_list

#level 3
#3.1 & 3.2 

