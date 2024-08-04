#1. Declare an empty list
empty_list=[]

#2. Declare a list with more than 5 items
animes=['Naruto','Black Clover','Bleach','Attack on Titan','Sailor Moon','Sword Art Online']
print(animes)

#3. Find the length of your list
print(len(animes))

#4. Get the first item, the middle item and the last item of the list
first_item=animes[0]
middle_item=animes[3]
last_item=animes[5]
print('The first item is:', first_item)
print('The middle item is:', middle_item)
print('The last item is:', last_item)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Will', 25, '5 ft 7','Single','Willsworld']
print(mixed_data_types)
print('My name is', mixed_data_types[0], 'I am', mixed_data_types[1], 'years old, my height is', mixed_data_types[2], 'yes I am', mixed_data_types[3], 'but I am happy, and just so you know I live in', mixed_data_types[4])

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
first_company=it_companies[0]
middle_company=it_companies[3]
last_company=it_companies[6]
print('The first company in this list is:', first_company)
print('The middle company in this list is:', middle_company)
print('The last company in this list is:', last_company)

#10. Print the list after modifying one of the companies
#modify in this context meant adding a list lol, at first I was going to pop it 
it_companies[0]='Kaseya'
print(it_companies)

#11. Add an IT company to it_companies
#you can use the append method to add an item to a list
it_companies.append('Github')
print(it_companies)

#12.Insert an IT company in the middle of the companies list
last=(len(it_companies))
middle=int(last/2)
it_companies.insert(middle, 'Wally')
print(it_companies)

#13.Change one of the it_companies names to uppercase (IBM excluded!)
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies.append('GOOGLE')
print(it_companies)

#14. Join the it_companies with a string '#;  '

it_companies.


 



