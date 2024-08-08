'''
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
'''
#1 . Find the length of the set it_companies
it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
print('There are', len(it_companies), 'IT companies in the set: it_companies')

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('We still are not including X in this set lol', it_companies)

#3. Insert multiple IT companies at once to the set it_companies
it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
new_it_companies={'Kaseya','Slack','Salesforce','NVDIA','Dell'}
it_companies.update(new_it_companies)
print('We have added more companies to the set:', it_companies)

#4. Remove one of the companies from the set it_companies
it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
#you can remove a random value with pop and return the value to you
it_companies.pop()
print('After popping, our set of companies is:', it_companies)
#remove, specify a element to remove but will error if the element is not present in the set
it_companies.remove('Facebook')
print('This time I went after Facebook, so the companies in this set are:', it_companies)
#discard, I could also use discard but this will not throw an error if the item is not present in the set as you will see
it_companies.discard('lime')
print('There was never a lime company in this set, so? what exactly were you thinking?')

#5. What is the difference between remove and discard
'''Remove throws an error if the element is not present in the set, and discard does not  throw an error if the element is not present in the set.'''

#Exercises: Level 2
#1. Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print('The union of these two sets yields:', C)

#2. Find A intersection B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('The intersection of A B is:', A.intersection(B))

#3. Is A subset of B
print('Is A a subset of B?', A.issubset(B))

#4. Are A and B disjoint sets
print('Are A and B disjoint sets?', A.isdisjoint(B))

#5. Join A with B and B with A
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A_B=A.union(B)
print('A joined to B is:', A_B)
B_A=B.union(A)
print('B joined to A is:', A_B)

#6. What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print('The symmetric difference between A and B is:', A.symmetric_difference(B))

#7. Delete the sets completely 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
del(A,B)
print(A)

#Exercises: Level 3
#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set=set(age)
print('The length of the age list is:', len(age), 'While the length of the list of the age set is:', len(age_set))
print(len(age) >= len(age_set))

#Explain the difference between the following data types: string, list, tuple and set
'''
String = any data that is in text 
List = ordered collection of items, modifiable, allows duplicate members.
Tuple = Ordered collection, not modifiable, allows duplicate members. 
Set = unordered collection, modifiable, no duplicate members. 
'''

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words. 
sentence='I am a teacher and I love to inspire and teach people'
print('The length of the sentence is:',(len(sentence)))
#there has to be some easier way to do this because wow that was miserable. 
#yea string splitting you idiot. 
words=[sentence[0], sentence[2:4], sentence[5], sentence[7:14], sentence[15:18],sentence[21], sentence[21:25], sentence[26:28], sentence[29:36],sentence[37:40],sentence[-12:-7],sentence[-7:53]]
print(words)
words_set=set(words)
#Make sure you learn........ 
words_split=sentence.split()
print(words_split)
print('The amount of unique words in this set is:', len(words_set), 'those words are:', words_set)