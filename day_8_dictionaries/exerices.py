#1. Create an empty dictionary called dog
dog=dict()
print('You created an empty dictionary and we called it', dog)

#2. Add name, color, breed, legs, age to the dog dictionary
dog.update['name':'bella','breed':'american stafford','legs':'4','age':'5']
#NOPE to the above, adding stuff to a dictionary is as simple as assigning the key:value pair
dog['name']='Bella'
dog['breed']='American Stafford'
dog['legs']='4'
dog['age']='5'
print('We have added new key:value pairs to the dog dictionary they are:', dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={'first_name':'Will','last_name':'Rodriguez','gender':'Male','Age':'26','Marital Status':'Single','Skills':['Chemistry', 'Art', 'Weightlifting', 'Crying'],'Country':'USA','Address':'Wills World.com'}
print('The content of the student dictionary is:', student)

#4. Get the length of the student dictionary
print('The length of the student dictionary is:', len(student), 'this is telling me how many key:value pairs we should see in the dictionary')

#5. Get the value of skills and check the data type, it should be a list
#Yikes bc I may have defined this skill to be a set data type, lists are better because a list can grow like me :)
student_skills=student.get('Skills')
print('Currently, the student has the following skills:',student_skills)
print('The skills key in the dictionary is a', type(student_skills), 'data type')

#6. Modify the skills values by adding one or two skills
#1a declare the dictionary
student={'first_name':'Will','last_name':'Rodriguez','gender':'Male','Age':'26','Marital Status':'Single','Skills':['Chemistry', 'Art', 'Weightlifting', 'Crying'],'Country':'USA','Address':'Wills World.com'}
#2a add values to the skills key in the student dictionary
student['Skills']='Python','Networking'
#Wrong i needed to use the append method, this above was overwrritng my skills portion to only mention python/networking; also need to get more comfortable understanding how many arguments I can give a function! 
student={'first_name':'Will','last_name':'Rodriguez','gender':'Male','Age':'26','Marital Status':'Single','Skills':['Chemistry', 'Art', 'Weightlifting', 'Crying'],'Country':'USA','Address':'Wills World.com'}
student['Skills'].append('Python')
student['Skills'].append('Networking')
print('The student has added more skills to their repetoire this summer, now the student can:', student['Skills'])

#7 Get the dictionary keys as a list
print('The keys to the student dictionary are:', student.keys())

#8. Get the dictionary values as a list
print('The dictionary values are:', student.values())

#9. Change the dictionary to a list of tuples using items() method
#1 declare the dictionary
student={'first_name':'Will','last_name':'Rodriguez','gender':'Male','Age':'26','Marital Status':'Single','Skills':['Chemistry', 'Art', 'Weightlifting', 'Crying'],'Country':'USA','Address':'Wills World.com'}
#2 change it to tuple using items()
student_tuple=student.items()
#3 print our student tuple 
print('The student dictionary printed as a tuple is:',student_tuple)

#10. Delete one of the items in the dictionary
#1 declare the dictionary:
student={'first_name':'Will','last_name':'Rodriguez','gender':'Male','Age':'26','Marital Status':'Single','Skills':['Chemistry', 'Art', 'Weightlifting', 'Crying'],'Country':'USA','Address':'Wills World.com'}
#2 delete one of the items in the dictionary
'''
Remember you have these options to delete stuff from dictionaries
- pop(key): remove item with specified key name
- popitem(): remove last item
- del: remove item with specified key name
'''
student.popitem()
#3 print the dictionary now that we deleted one of the items in it? 
print('Now that we deleted one of the items, lets see what the content is:',student)
#My address was deleted

#11. Delete one of the dictionaries
#1 declare the dictionary:
student={'first_name':'Will','last_name':'Rodriguez','gender':'Male','Age':'26','Marital Status':'Single','Skills':['Chemistry', 'Art', 'Weightlifting', 'Crying'],'Country':'USA','Address':'Wills World.com'}
# delete the dictionary
del(student)
# print to see if its still there or not 
print('Does the dictionary exist anymore?', student)
''' File "<string>", line 7, in <module>
NameError: name 'student' is not defined'''


