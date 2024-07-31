#Day 2: 30 Days of Python programming

#Variable declaration practice
first_name='Will '
last_name='Rodriguez'
full_name=(first_name + last_name)
country='Floridaland'
city='305Nation'
age=26
year=2024
is_married=False
is_true = True
is_light_on = True

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Will','Rodriguez',(first_name + last_name), 'Floridaland', '305Nation', 26, 2024, False, True, True, 

#Level 2

#Check data type of all the variables we just declared
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#using the length function what is the length of first name (keep in mind I put a space there so it looks good); i got 4 as my answer so cool!
print(len(first_name))
print(len(last_name))
print('Difference between first/last name is: ', (len(last_name) - len(first_name)))

```
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp

Figure out what the fuck that means
Find floor division of num_one by num_two and assign the value to a variable floor_division
```
num_one=5
num_two=4

total = num_one + num_two
print('total is ', total)

diff = num_two - num_one
print('difference is ', diff)

product = num_one * num_two
print('product of two is, ', product)

division = num_one / num_two
print('Quotient of num_one/num_two is', division)

remainder = num_one % num_two
print('Modulus 5 of 4 is', remainder)

exp = num_one ** num_two
print('Number One raised to the power of number two is', exp)

```The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords```

#area_of_circle = pi*(r)**2, in this instance i will use pi = 3.14

area_of_circle = 3.14*(30)**2
print('Area of circle is:', area_of_circle, 'meters squared')

#circumference is usually 2*pi*r
circum_of_circle= 2*3.14*30
print('The circumference of the Circle is:', circum_of_circle, 'meters')

#Take radius as user input and calculate the area.
radius=input('For what radius would you like to calculate the area of a circle for?')
#need to convert this input from string to integer
```The key to making this work was by getting the user input and casting its value from string data type to integer data type so i could use that variable in the multiplication operation that occurs when getting the area, that way I am not multiplying numbers with strings```
int_radius=int(radius)
units=input('What units is the radius measured in?')
area = 2*3.14*int_radius
print('The calculated area is', area, units)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

_first_name=input('What is your first name?')
_last_name=input('What is your last name?')
_country=input('Where are you from?')
_age=input('How old are you?')
print('Based off the provided information you are', _first_name, _last_name, 'from', _country, _age, 'years of age, thanks for coming to Wills World!')

#Help for the keywords in python 
print(help('keywords'))