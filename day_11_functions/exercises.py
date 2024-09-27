#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    count = num1 + num2
    return count
print('The sum of your two numbers are:', add_two_numbers(10,10))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
    area = 3.14 * r ** 2
    return area
print('The area of a circle with radius = 2 is', area_of_circle(2))

#3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0 
    for num in nums:
        total = total + num
    return total
print('The sum of all the numbers is', add_all_nums(10,20,30))
#This works but I need to figureout the reasonable feedback 
#coming back to that part

def add_all_nums(*nums):
    total = 0 
    for num in nums:
        total += num
    if total != int:        
        print('Please pass this function integer arguments!')
        return total
print('The sum of all the numbers is', add_all_nums(10,20,30))

#4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(C):
    fahrenheit = (C * 1.8) + 32
    return fahrenheit
print('The temperature you gave in celsius is', convert_celsius_to_fahrenheit(20))

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
#This worked because I set month check = to a string and then used a conditional operator to say if month is in this list of months month check should be set to a season and return that value. 
def check_season(month):
    month_check=''
    if month in ['November','December','January']:
        month_check='Winter'
    elif month in ['February','March','April']:
        month_check='Spring'
    elif month in ['May','June','July']:
        month_check='Summer'
    elif month in ['August','September','October']:
        month_check='Fall'
    else:
        print('Did you even select a month?')
    return month_check
print("Based off the month you picked, the season corresponds to", check_season('December'))
print("Based off the month you picked, the season corresponds to", check_season('March'))
print("Based off the month you picked, the season corresponds to", check_season('August'))
print("Based off the month you picked, the season corresponds to", check_season('May'))
print("Based off the month you picked, the season corresponds to", check_season('6'))

#6. Write a function called calculate_slope which return the slope of a linear equation
#slope is y = mx + b

def calculate_slope(y,x,b):
    slope = (y-b)/x
    return slope
print('Using the equation of the line and the points provided, the slope of this line is', calculate_slope(10,3,2)) 

#7 stuck: Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a,b,c):
    solution_set=

#dawg i aint even like this kind of a question in algebra, next!

#8. Stuck: Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(listy):
    printed_list=list(listy)
    return printed_list
print('The list you entered to us is', print_list(['Will','Rodriguez','Infocyte','QA:)']))
# this prints the list but I think the question wants each individual item, not the list itself

def print_list2(*items):
    item=list(items)
    counter = 0
    while len(item) >= 0:
        print(item[len(item)])
print_list2('help','there','charlie')

#define the function print_list

#put fruits in the fruit list 

# use what I know about lists to print the elements in the list

# save those prints to a var and return the var? 
def print_list(*input_list):
    arg_list=[input_list]
    result_list = []
    counter = len(arg_list)
    while counter >= 0:
        result_list.append(arg_list[counter])
        counter - 1
    return result_list
print('The resulting list you gave us is', print_list('Will','Rodriguez'))



#9 Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
'''
what I did in the loops section to get this to work

1. declare a list variable
fruits=['banana', 'orange', 'mango', 'lemon']

2. using a for loop with range 
so for integers in the range of length of my fruit list -1, ending at -1 with a -1 step
for i in range(len(fruits) - 1, -1, -1):

3. declare a variable called  the reversed_list and append the items to that list from the intitial list
    reversed_fruits.append(fruits[i])
4. print the list 
print(reversed_fruits)

'''

def reverse_list(*items):
    reversed_list=[]
    for i in range(len(items)-1, -1, -1):
        reversed_list.append(items[i])
    return reversed_list
print('your list reversed is', reverse_list('Apple','Banana','Orange','Mango'))

items=['Apple','Banana','Orange','Mango']
print(len(items))
print(range(len(items)-1,-1,-1))
#does it not matter to range that in in this list there is no index -1, does the code just not give a rat and move on 

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# define the list

# NOPE: convert the list into strings
#YES: print each element of the list which is a string 
# use swapcase stringmethod to captialize the string

#this works but gives me a reversed capitalized list what about one in the right order
def capitalized_list(*items):
    capital_items=[]
    for i in range(len(items)-1,-1,-1):
        capital_items.append(items[i].swapcase())
    return capital_items

print('The capitalized list of items you gave us is,', capitalized_list('will','rodriguez','infocyte'))    

def capitalized_list(*items):
    capital_items=[]
    for i in range(0,len(items),1):
        capital_items.append(items[i].swapcase())
    return capital_items

print('The capitalized list of items you gave us is,', capitalized_list('will','rodriguez','infocyte'))    

#This works! 
#Kinda easier when I approach the problem and go oh maybe I should look at using this, this and this


#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# make the list
# add the item to said list
# print the list 

snack_list=['Apple','Banana','Cranberry','Doritos']
def add_item(snack_list, *items):
    for item in items:
        snack_list.append(item)
    return snack_list
print('After adding your new selections, the current snack list is', add_item(snack_list, 'Fruit Loops','Gushers'))