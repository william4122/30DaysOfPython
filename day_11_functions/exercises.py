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
        total += num
    return total
print('The sum of all the numbers is', add_all_nums(10,20,30))
#This works but I need to figureout the reasonable feedback 

def add_all_nums(*nums):
    total = 0 
    for num in nums:
        total += num
        if add_all_nums(*nums) != int:
            return 'The function was passed a non-integer number so we cannot add this, please pass this function integer arguments!'
    return total

print('The sum of all the numbers is', add_all_nums(10,20,30))