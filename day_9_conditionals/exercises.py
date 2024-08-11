#1
'''
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
'''

age=int(input('Enter your age in years:'))
if age >= 18:
    print('You are', age, 'so you are old enough to drive kiddo, be safe!')
else:
    print('You need', 18-age, 'years to learn to drive, keep waiting champ')

#2. 
'''
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
Enter your age: 30
You are 5 years older than me.
'''
your_age=30
my_age=int(input('Enter your age in years:'))
if your_age - my_age == 1:
    print('We have a one year age gap')
elif your_age - my_age > 1:
    print('We have a age gap bigger than one year, our age gap is', your_age-my_age, 'years.')
elif your_age - my_age ==0:
    print('We are the same age! Twinsies')

'''
#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
Enter number one: 4
Enter number two: 3
4 is greater than 3
'''

number_one=int(input('Pick a number for number 1:'))
number_two=int(input('Pick a number for number 2:'))
if number_one > number_two:
    print(number_one,'>', number_two)
elif number_one < number_two:
    print(number_one, '<', number_two)
elif number_one==number_two:
    print('The two numbers you picked are equal to each other.')


# Exercises level 2 
#1. Write a code which gives grade to students according to theirs scores:
'''
90-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''
student_score=int(input('What score did you get on your exam?'))
if student_score <= 100 and student_score >= 90:
    print('You got a', student_score, 'based off our grading scale that is an A, excellent job!')
elif student_score <=89 and student_score >=70:
    print('You got a', student_score, 'based off our grading scale this would be a B, good work!')
elif student_score <=69 and student_score >=60:
    print('You got a', student_score,'which based off our grading scale is a C, consider reviewing for improvement')
elif student_score <=59 and student_score >=50:
    print('You got a',student_score,'in our grading system this is a D, so you need to study harder if you do not want to fail.')
elif student_score <= 49 or student_score==0:
    print('You got a', student_score,'that is an F in our scale, so you will fail if you continue this route.')
else:
    print('Did you even take a test?')

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month=input('What month of the year is it currently?')
if month == ('September'):
    print('Based off the month in the year the season is Autumn')
elif month == ('October'):
        print('Based off the month in the year the season is Autumn')
elif month == ('November'):
    print('Based off the month in the year the season is Autumn')
elif month == ('December'):
    print('Based off the month you picked if you are in the northern hemisphere the season should be Winter')
elif month == ('January'):
    print('Based off the month you picked if you are in the northern hemisphere the season should be Winter')
elif month == ('February'):
    print('Based off the month you picked if you are in the northern hemisphere the season should be Winter')
elif month == ('March'):
    print('Based off the month of the year you selected, if you are living in the northern hemisphere you should be in the Spring season')
elif month == ('April'):
    print('Based off the month of the year you selected, if you are living in the northern hemisphere you should be in the Spring season')
elif month == ('May'):
    print('Based off the month of the year you selected, if you are living in the northern hemisphere you should be in the Spring season')
elif month == ('June'):
    print('Based off the months you selected if you are living in the Northern Hemisphere you should be in the Summer season.')
elif month == ('July'):
    print('Based off the months you selected if you are living in the Northern Hemisphere you should be in the Summer season.')
elif month == ('August'):
    print('Based off the months you selected if you are living in the Northern Hemisphere you should be in the Summer season.')
else:
    print('Are you even on Planet Earth?')

# I could have done this more effectively using the in operator of the seasons
month = input('What month of the year is it currently?')
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
if month in autumn:
    print('Based on the month of the year, the season is Autumn.')
elif month in winter:
    print('Based on the month you picked, if you are in the northern hemisphere, the season should be Winter.')
elif month in spring:
    print('Based on the month of the year you selected, if you are living in the northern hemisphere, you should be in the Spring season.')
elif month in summer:
    print('Based on the months you selected, if you are living in the Northern Hemisphere, you should be in the Summer season.')
else:
    print('Are you even on Planet Earth?')

#3. The following list contains some fruits:
#fruits = ['banana', 'orange', 'mango', 'lemon']
#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
#thank you comparison operators! :D 
fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit=input('What fruit would you like to add to our list?')
if user_fruit in fruits:
    print('This fruit already exists in the list but you do have great taste!')
elif user_fruit not in fruits:
    fruits.append(user_fruit)
    print('We have added your request to our list and now all of the fruits are:', fruits)

#Exercises - Level 3
#4. Here we have a person dictionary. Feel free to modify it!
'''
 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:
'''

person={
    'first_name': 'Will',
    'last_name': 'Rodriguez',
    'age': 260,
    'country': 'USA',
    'is_marred': False,
    'skills': ['Chemistry', 'Crying', 'Weightlifting', 'SQL', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '77411'}
}
#1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    #Just an fyi while this works it might be easier if I just do integer division // middle_skill = (len(person['skills']) - 1) // 2
    middle_skill=int((len(person['skills'])-1)/2)
    print('The middle skill in the skills list is:', person['skills'][middle_skill])
#2 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
    print('The dictionary has a skills key and since it has Python in the values, the rest of the skills this person has are:', person['skills'])
else:
    print('The dictionary does not have a skills key, so it seems as if the person does not have skills which is unlikely.')


#3.  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
person={
    'first_name': 'Will',
    'last_name': 'Rodriguez',
    'age': 260,
    'country': 'USA',
    'is_marred': False,
    'skills': ['Python','Node','MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '77411'}
}
person_skills=person['skills']
if 'skills' in person and 'JavaScript' in person_skills and 'React' in person_skills:
    print('Based off the skills provided this person seems to be a front-end developer')
elif 'Node' in person_skills and 'Python' in person_skills and 'MongoDB' in person_skills:
    print('Based off the skills in this list this person is likely a backend developer')
elif 'React' in person_skills and 'Node' in person_skills and 'MongoDB' in person_skills:
    print('Based off the skills in this list, this person seems to be a full stack developer')
else:
    print('This person does not seem to be a developer, we do not know what position they hold but these are there skills:', person['skills'])


#I think were I f'ed up in this problem was thinking that the words for the comparison operators were word1 and word2 and word3 in word_list but in reality its word1 in word_list and word2 in word_list and word3 in word_list

#4. Man that other question is hard:
# * If the person is married and if he lives in Finland, print the information in the following format: first_name last_name lives in country. He is married.
person={
    'first_name': 'Will',
    'last_name': 'Rodriguez',
    'age': 260,
    'country': 'USA',
    'is_married': False,
    'skills': ['JavaScript','React'],
    'address': {
        'street': 'Space street',
        'zipcode': '77411'}
}
if person['is_married'] == True:
    print('%s %s lives in %s. He is married' %(person['first_name'], person['last_name'], person['country']))
else:
    print('%s %s lives in %s. He is not married' %(person['first_name'], person['last_name'], person['country']))