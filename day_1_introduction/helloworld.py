print(
      'python', 'version'
)

#will not work with arithmetic operators
#print('4 + 3')

## will work with arithmetic 
print(
    4 + 3
)

print(3-4)

print(3*4)

print(3%4)

print(3/4)

print(3**4)

print(3//4)

#printing strings because thats not all we write here

print('My name is Will, the legendary hero who will learn from the Avalokiteśvara statue')

print('My last name is Rodriguez')

print('I am from the United States of America')

print('I am enjoying the 30 days of python class')

#now to print checking data types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type('Will''Ummm''Cuba'))
print(type('will'))
print(type('rodriguez'))
print(type('usa'))

```
for some reason this will return the following error 

print(type('Will','Ummm','Cuba'))
Traceback (most recent call last):
  File "d:\30DaysOfPython\day_1\helloworld.py", line 40, in <module>
    print(type('Will','Ummm','Cuba'))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: type.__new__() argument 2 must be tuple, not str

but this works fine??????
print(type('Will''Ummm''Cuba'))
```

#level 3

#xample for each data type: Number (integer, float, complex) string, boolean, list, tuple, set, dictionary

#Numbers
```
Integer = -1,0,1 
Float = 9.8
Complex = 1i

String = 'Will ligma'
Boolean = T/F
List = 'hey', 'will'
or = 'hey','111','2i'
tuple = same thing as a list but can't be modified, still ordered  
set = list but not ordered 
dictionary = {
    "name":"will",
    "last_name":"rodriguez",
    "age":"none-ya"
    "iq":"1i"
}
```


#Find an Euclidian distance between (2, 3) (p1, p2) and (10, 8) (q1, q2)
#The formula is a2 + b2 = c2
#when you have two coordinate points the euclidian distance between the two is ((p1-q1)**2 + (p2-q2)**2)**0.5
p1 = 2
p2 = 3

q1 = 10
q2 = 8 

answer = ((p1-q1)**2 + (p2-q2)**2)**0.5
distance = answer

print('distance')