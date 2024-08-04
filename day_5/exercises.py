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

it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
it_companies_joined=(it_companies[0] + '#;  ', it_companies[1] + '#;  ', it_companies[2] + '#;  ', it_companies[3] + '#;  ', it_companies[4] + '#;  ', it_companies[5] + '#;  ', it_companies[6] + '#;  ')
print(it_companies_joined)

#15. Check if a certain company exists in the it_companies list.
it_companies=['Facebook','Amazon','Google','IBM','Microsoft','Oracle']
twitter_exist=it_companies.index('Twitter')
print(twitter_exist)

#can also do
twitter_exist=it_companies.count('Twitter')
print(twitter_exist)
 
#so far I have gotten either a name error or a 0 count. is there a way to get boolean?

#16. Sort the list using sort() method
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.sort()
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
#we slice out a list using  indexes 
it_companies_first3_sliced=it_companies[3:6]
print(it_companies_first3_sliced)
#or
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies_first3_sliced=it_companies[-4:-1]
print(it_companies_first3_sliced)

#19. Slice out the last 3 companies from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies_last3_sliced=it_companies[0:4]
print(it_companies_last3_sliced)

#20. Slice out the middle IT company or companies from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies_middle=it_companies[3]
print(it_companies_middle)

#21. Remove the first IT company from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.remove('Facebook')
print(it_companies)
#or
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.pop(0)
print(it_companies)

#22. Remove the middle IT company or companies from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.remove('IBM')
print(it_companies)
#or with pop 
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.pop(3)
print(it_companies)

#23. Remove the last IT company from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.remove('Apple')
print(it_companies)
# or with pop, no need to specify an index; pop removes the last one by default. 
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.pop()
print(it_companies)

#24. Remove all IT companies from the list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
it_companies.clear()
print(it_companies)

#25. Destroy the IT companies list
it_companies=['Facebook','Google','Amazon','IBM','Oracle','Microsoft','Apple']
del it_companies
print(it_companies)

'''
#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
'''
front_end=['HTML','CSS','JavaScript','React','Redux']
back_end=['Node','Express','MongoDB']
full_stack=front_end + back_end
print(full_stack)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
front_end=['HTML','CSS','JavaScript','React','Redux']
back_end=['Node','Express','MongoDB']
full_stack=front_end + back_end
full_stack2=full_stack.copy()
#looks like the index argument for .insert is the index(position) you want to put the 2nd argument in.
full_stack2.insert(5, 'Python')
full_stack2.insert(6, 'SQL')
print(full_stack2)


#Exercises: Level 2
'''
#1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
'''
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('Now that we have sorted the list we know the minimum age is the first element, and the maximum age is the last elemenet in the list')
print('Minimum age:', ages[0], 'Maximum age:', ages[-1])

min_age=ages[0]
max_age=ages[-1]
ages.append(min_age)
ages.append(max_age)
print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages=[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
ages.sort()
print(ages)
median_age_index=int(len(ages)/2)
median_age=int(ages[median_age_index]/2)
print(median_age)

#Find the average age (sum of all items divided by their number )
ages=[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
print(len(ages))
index_number=len(ages)
#I think I could have done this sum better but oh well
sum=(ages[0]+ ages[1]+ages[2]+ages[3]+ages[4]+ages[5]+ages[6]+ages[7]+ages[8]+ages[9]+ages[10]+ages[11])
print(sum)
#Making this an integer because floats don't exist with age loll
average=int(sum/index_number)
print('The average age in this list is', average, 'years')


#Find the range of the ages (max minus min)
ages=[19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 19, 26]
ages.sort()
max=ages[-1]
min=ages[0]
range=max-min
print('The range of the ages is',range,'years')

#Compare the value of (min - average) and (max - average), use abs() method
#from the previous question we know that average=22, min=19, max=26
average=22
min=19
max=26

min_value=(min-average)
max_value=(max-average)

print('The minimum value - average is', min_value, '. The maximum - average is', max_value)

#Find the middle country(ies) in the countries list
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

middle_country_index=int(len(countries)/2)
print('The middle country from this list is:', countries[middle_country_index])

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
before_middle=middle_country_index-1
beg_middle=countries[0:before_middle]
middle_end=countries[middle_country_index::]
print('From beginning to before the middle, the list is', beg_middle, 'but from middle -> end the list of countries is', middle_end)


#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
last_list=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
superpower_countries=last_list[0:3]
scandic_countries=last_list[3::]
print('The super-power countries of the world are:', superpower_countries, 'The scandic countries of the world in this list are:', scandic_countries)
