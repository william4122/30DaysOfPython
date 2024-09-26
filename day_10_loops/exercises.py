#1 Iterate 0 to 10 using for loop, do the same using while loop.

# I messed up here, I need to actually do this
count = 0
while count < 11:
    print(count)
    count = count + 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
count = 10
while count > 0:
    print(count)
    count = count - 1
#for this one I did not need to start it at count = 10

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# To me this is a question I need some guidance on, I can get the loop to print the hashtag triangle but it does not look like the answer I see in github, it looks like a list 
  #
  ##
  ###
  ####
  #####
  ######
  #######

triangle = list('#')
while len(triangle) < 7:
    print(triangle)
    triangle.append('#')

'''
['#']
['#', '#']
['#', '#', '#']
['#', '#', '#', '#']
['#', '#', '#', '#', '#']
['#', '#', '#', '#', '#', '#']
'''

triangle = list('#')
while len(triangle) < 7:
    print(triangle)
    triangle.insert(0,'#')

'''
['#']
['#', '#']
['#', '#', '#']
['#', '#', '#', '#']
['#', '#', '#', '#', '#']
['#', '#', '#', '#', '#', '#']
'''

triangle = list('#')
while len(triangle) < 7:
    print(triangle)
    triangle.extend('#')
'''
['#']
['#', '#']
['#', '#', '#']
['#', '#', '#', '#']
['#', '#', '#', '#', '#']
['#', '#', '#', '#', '#', '#']
'''

#4. Use nested loops to create the following: need help here lol 

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

triangle = list('#')
while len(triangle) < 8:
    triangle.append('#')
for triangle < 8:
print(triangle)

triangle_list = [[j for j in range('#')] for i in range(8)]
print(triangle_list)

#5. Print the following pattern:

'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''

list_one = range(10)
list_two = range(10)
for i in list_one:
    for j in list_two:
        print(i, 'x', j, '=', i * j)


#nope, this gives you 

'''0 x 0 = 0
0 x 1 = 0
0 x 2 = 0
0 x 3 = 0
0 x 4 = 0
0 x 5 = 0
0 x 6 = 0
0 x 7 = 0
0 x 8 = 0
0 x 9 = 0
1 x 0 = 0
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
2 x 0 = 0
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
3 x 0 = 0
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
4 x 0 = 0
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
6 x 0 = 0
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
7 x 0 = 0
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
8 x 0 = 0
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
9 x 0 = 0
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
'''

list_one = range(11)
list_two = range(11)
for i in list_one:
    for j in list_two:
        if i == j:
            print(i, 'x', j, '=', i * j)
        if i != j:
            continue

'''
This worked! 
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
'''

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
pskills=['Python', 'Numpy','Pandas','Django', 'Flask']
for skill in pskills:
    print(skill)

'''
Python
Numpy
Pandas
Django
Flask
'''

#7. Use for loop to iterate from 0 to 100 and print only even numbers
numbers=range(101)
for i in numbers:
    if i % 2 == 0:
        print(i)
    else:
        continue

'''
This worked because I used the remainder operator, if the remainder of division by 2 = 0 we have an even number so lets print it 
0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100'''

#8 Use for loop to iterate from 0 to 100 and print only odd numbers
numbers=range(101)
for i in numbers:
    if i % 2 != 0:
        print(i)
    else:
        continue

'''
This worked with the same code from q 7 I just had to modify the comparison to be not equal to 0 bc if remainder of division by 2 does not = 0 you have an even number
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
39
41
43
45
47
49
51
53
55
57
59
61
63
65
67
69
71
73
75
77
79
81
83
85
87
89
91
93
95
97
99
'''

# Exercises Level 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers. I ended up getting help for this one 
#For loop 
total_sum = 0 
for number in range(101):
    total_sum += number
print('The sum of all the numbers is', total_sum)


#cheapp way of getting the answer:
numbers=list(range(101))
print('The sum of all the numbers is', sum(numbers))

#2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
total_sum_odds= 0
for number in range(101):
    if number % 2 != 0:
        total_sum_odds += number
total_sum_evens= 0
for number in range(101):
    if number % 2 == 0:
        total_sum_evens += number
print('The sum of all the odd numbers is', total_sum_odds, 'The sum of all the even numbers is', total_sum_evens)


#Exercises: Level 3
#1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

for country in countries:
    if country.endswith('land') == True:
        print(country)

'''
Finland
Iceland
Ireland
New Zealand
Poland
Swaziland
Switzerland
Thailand
'''

#2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon']
for fruit in fruits:
    print(fruit[::-1])

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print(reversed_fruits)


'''
Go to the data folder and use the countries_data.py file.
What are the total number of languages in the data
Find the ten most spoken languages from the data
Find the 10 most populated countries in the world

'''