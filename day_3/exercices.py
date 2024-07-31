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

#5. Write a script that allows you to enter sides a, b, c of a triangle; calculate permiter which is a + b+ c 
a=int(input('enter side a'))
b=int(input('enter side b'))
c=int(input('enter side c'))
perimeter=a+b+c
print('the perimeter of the triangle based off the provided measurements is', perimeter)

#6. Get length and width of triangle using a prompt. Calculate area(length*width), perimeter (2x(length+width))
length=int(input('What is the length of the triangle?'))
width=int(input('What is the width of the triangle?'))
area=length*width
perimeter6=(2*(length+width))
print('Based off the provided measurements, the triangle has a perimeter equal to', perimeter6, 'and the area of the triangle is', area)

#7.Get radius of a circle using a prompt; calculate area (3.14 * r**2) and circumference (c = 2 * 3.14 * r)
radius=int(input('what does the circle radius measure?'))
area=(3.14*radius**2)
circumference=(2*3.14*radius)
print('Based off your measurements, the results are area =', area, 'and circumference =', circumference)

#8. Calculate the slope, x-intercept/y-intercept of y = 2x -2
#m=(y-b)/x
```
y + 2 = 2x

y+2/x = 2

```


#9. Slope is (m = y2-y1/x2-x1) find slope & euclidean distance between (2,2) and (6,10)
x1=2
y1=2
x2=6
y2=10
slope=(y2-y1)/(x2-x1)
print('slope is equal to:', slope)
#from the last time I used this to calculate the euclidean
#distance = ((p1-q1)**2 + (p2-q2)**2)**0.5
euclidean_distance=((x1-y1)**2 + (x2-y2)**2)**0.5
print('The Euclidean distance between these two points is', euclidean_distance)

#10. compare the two slopes you got from 8/9

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

#12. Find the length of 'python' and 'dragon' and make a false comparison statement.
python_length=len('python')
print('the length of python is', python_length)
dragon_length=len('dragon')
print('the length of dragon is', dragon_length)
print('python' in 'dragon')

#13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python')
on_python='on' in 'python'
on_dragon='on' in 'dragon'
print(on_dragon)
#the and operator returns true because both of these variables have been assgined a boolean of True. This is because when I used the 'in' comparison operator I got true/false
print(on_python and on_dragon)

#14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print('jargon' in 'I hope this course is not full of shit')

#15. There is no 'on' in both dragon and python
#Just needed to add my not to make it negate the truth :) 
on_python='on' in 'python'
on_dragon='on' in 'dragon'
print(not(on_python and on_dragon))

#16. Find the length of the text python and convert the value to float and convert it to string
print(len('python'))
python_length=len('python')
float_python_length=float(python_length)
print(float_python_length)
string_python_length=str(python_length)
print(string_python_length)

#17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
#modulus gives me the remainder of the division. so if the modulus is = to 0 should it not mean we have a even number? 
num_1=int(input('What number do you want to check if its even?'))
even_test=(num_1 % 2)
if even_test > 0:
    print('this is an odd number')
else: print('this is an even number')

#18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == int(2.7))

#19.Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#20. Check if int('9.8') is equal to 10
print(int(9.8)== 10)

#21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours_worked=int(input('How many hours did you work this week?'))
hourly_rate=int(input('How much do you get paid per hour?'))
weekly_earning=hours_worked * hourly_rate
print('Working', hours_worked, 'hours for', hourly_rate, 'an hour gives you a weekly yield of', '$',weekly_earning, 'good job! and don`t forget to treat yourself!')

#22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
age=int(input('How old are you?'))
```
365 day/year * 24 hour/day * 60 min/hour * 60 seconds/min = seconds/year
```
seconds_in_year=(365*24*60*60)
seconds_lived=(age*seconds_in_year)
seconds_in_century=(seconds_in_year*100)
seconds_left=seconds_in_century-seconds_lived
print('Based off your age, you have lived', seconds_lived, 'seconds; with that being said, you have', seconds_left, 'seconds left till 100!')

#23. Write a Python script that displays the following table
```
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
```
#all this seems to doing is printing the exponents of a number starting from 0 -> 3
#i looked up the solution here lol
print(1, 1**0, 1**1, 1**2, 1**3)
print(2, 2**0, 2**1, 2**2, 2**3)
print(3, 3**0, 3**1, 3**2, 3**3)
print(4, 4**0, 4**1, 4**2, 4**3)
print(5, 5**0, 5**1, 5**2, 5**3)
