#1. Filter  only negative and zero in the list using list comprehensionv
#numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [ i - (i + i) for i in range(6)]
print(numbers)
'''
>>> print(numbers)
[0, -1, -2, -3, -4, -5]
'''

'''While my answer does give a list with negative numbers and 0 it does not filter out my current list
Correct answer
'''

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [i for i in numbers if i <= 0]
print(filtered_numbers)

#2. Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list= [number for row in list_of_lists for number in row]
print(flattened_list)
# I think I have to do this twice actually, because in the first example I had ]]
# Now with this as soon as I print I have ]]
second_flattened_list= [number for row in flattened_list for number in row]
print(second_flattened_list)

'''Some explanation over why the above is 3d and the other is 2d, levels of nesting through brackets; similar to nesting order of operations with parenthesis 

Exactly! You can think of that extra pair of brackets in a similar way to parentheses in math—they introduce another level of nesting, making the structure more complex.
'''
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
par_list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]


#3. Using list comprehension create the following list of tuples:
'''
[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]
'''

'''
From the notes
#It is also possible to make a list of tuples
numbers=[(i, i*i) for i in range(11)]
print(numbers)
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
'''

numbers=[(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(numbers)
# I was right that I couldve done a for loop to make this more elegant
numbers = [(i,) + tuple(i**j for j in range(6)) for i in range(11)]
print(numbers)


#4. Flatten the following list to a new list:

'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

'''

#so flatten this by one dimension
#should i append/capitalize before flattening?
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list= [number for row in countries for number in row]
countries[0].insert(1, [:3])
print(countries[0])
second_flattened_list

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [number for row in countries for row in countries for number in row]
print(countries)


'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Flatten the list by one dimension and format it
formatted_countries = [[country.upper(), country[:3].upper(), city.upper()] for sublist in countries for country, city in sublist]

print(formatted_countries)

'''

#5. Change the following list to a list of dictionaries:
'''
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
'''
#reduce this by one dimension
#make it uppercase with uppercase
#make it a dictionary with 2 keys: country/city

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries=[[country.upper(),city.upper()] for sublist in countries for country, city in sublist]
print(formatted_countries)
dict(formatted_countries) == {'country':'','city':''}
print(formatted_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
formatted_countries=[{'country': country.upper(),'city': city.upper()} for sublist in countries for country, city in sublist]
print(formatted_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Flatten the list and create a dictionary for each country and city pair
formatted_countries = [{'country': country.upper(), 'city': city.upper()} for sublist in countries for country, city in sublist]

print(formatted_countries)


#6. Change the following list of lists to a list of concatenated strings:
'''
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
'''

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
formatted_strings = [(firstname + ' ' + lastname) for sublist in names for firstname, lastname in sublist]
print(formatted_strings)
#nice i got this one right on my own 


#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
# y = mx + b
# or m = (y2 -y1)/(x2- x1)
# b = y- mx

slope = lambda y2, y1, x2, x1: (y2-y1)/(x2-x1)
print(slope(8,6,7,5))

y_intercept = lambda y, m : (y - m*0)
print(y_intercept(2,4))



