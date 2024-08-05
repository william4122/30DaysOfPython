#Exercises: Level 1
#1. Create an empty tuple
empty_tuple=()
print(empty_tuple)

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_brothers=('Alejandro','Elier')
my_sisters=('Yanary','Nelly','Normita')
print('Have you met my brothers:', my_brothers, 'Also, these are my sisters:', my_sisters)

#3. Join brothers and sisters tuples and assign it to siblings
my_siblings=my_brothers + my_sisters
print('My siblings are:', my_siblings)

#4. How many siblings do you have?
print('You have', len(my_siblings), 'total siblings')

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members=list(my_siblings)
family_members.append('Wilfredo')
family_members.append('Jackeline')
print('Now that we added mom & dad, our family memebers are', family_members)

#level 2
#1. Unpack siblings and parents from family_members
before_parents=len(family_members) - 2 
siblings=family_members[0:before_parents]
print('Your siblings are:', siblings)
parents=family_members[-2:]
print('Your parents are: ', parents)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits=('Strawberry','Blueberry','Grape','Banana')
vegetables=('Corn','Onion','Garlic','Kale')
animal_products=('Chicken','Steak','Salmon')
food_stuff_tp=fruits + vegetables + animal_products
print('All the food you have written is: ', food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item=len(food_stuff_lt) // 2 
food_stuff_lt.pop(middle_item)
print(food_stuff_lt)
#you cant remove these items from the tuple because tuples are immutable 

#5. Slice out the first three items and the last three items from food_staff_lt list
#remove the first 3 items
food_stuff_lt.pop(0)
food_stuff_lt.pop(1)
food_stuff_lt.pop(2)
#remove the last 3 items
food_stuff_lt.pop(-1)
food_stuff_lt.pop(-2)
food_stuff_lt.pop(-3)
print('Since you removed from the list, we have', food_stuff_lt)

#6. Delete the food_staff_tp tuple completely
del(food_stuff_tp)
print('Deleted food tuple!')
food_stuff_tp

#7. Check if an item exists in tuple:
'''
Check if 'Estonia' is a nordic country
Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''

#Estonia:
nordic_countries=('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Is Estonia a nordic country?', 'estonia' in nordic_countries)
#Iceland:
print('Is Iceland a Nordic country?', 'Iceland' in nordic_countries)