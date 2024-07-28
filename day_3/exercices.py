#1. declare your age as a integer variable
my_age=26
print('My age is',my_age)

#2.Declare your height as a float variable
my_height=5.7
print('My height is', my_height,'feet')

#3. Declare a variable that stores a complex number
my_complex_number=1+1j
print('My first complex number is', my_complex_number)

#4. Write a script that prompts someone to enter base and height of a triangle and then calculate the area of said triange (area= 0.5 x base x height)
base=int(input('What is the height of the base of the triangle you want to calculate?'))
height=int(input('What is the height of the triangle you wish to calculate the area for?'))
units=input('What units are these measurements in?')

area=(0.5 * base * height)
print('based off your measurements the area of the triangle is', area, units)
