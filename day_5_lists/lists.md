# Lists

Four collection data types in Python

1. List: Collection (ordered, modifiable, allows duplicate members)

2. Tuple: collection (ordered, unchangeable, unmodifiable[immutable], allows duplicate members)

3. Set: Collection (unordered, unmodifiable-- *we can add new items to a set*, unindexed, no duplicate members)

4. Dictionary: collection (unordered, changeable[modifiable], indexed, no duplicate members)

## How to Create a List

Create a list in python in two ways

- Using the list built-in-function

```
>>> lst=list()
>>> empty_list=list()
>>> print(len(empty_list))
0
```

- Using square brackets []

```
>>> lst=[]
>>> empty_list=[]
>>> print(len(empty_list))
0
```

- An example of a list with an initial value. 
    - We use len() to find the length of a list 

```
>>> fruits=['banana', 'orange', 'mango', 'lemon']
>>> vegetables=['carrot','bell-pepper','corn','spinach','tomato']
>>> animal_products=['salmon','steak','chicken','eggs']
>>> web_techs=['HTML','CSS','JS','React','Redux','Node','MongoDB']
>>> countries=['United States','Canada','Mexico','Cuba']
>>> #Print the lists and its length 
>>> print('Fruits:', fruits)
Fruits: ['banana', 'orange', 'mango', 'lemon']
>>> print('Number of fruits:', len(fruits))
Number of fruits: 4
>>> print('Vegetables:', vegetables)
Vegetables: ['carrot', 'bell-pepper', 'corn', 'spinach', 'tomato']
>>> print('Number of vegetables:', len(vegetables))
Number of vegetables: 5
>>> print('Animal products:', animal_products) 
Animal products: ['salmon', 'steak', 'chicken', 'eggs']
>>> print('Number of animal products:', len(animal_products))
Number of animal products: 4
>>> print('Web technologies:', web_techs)
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
>>> print('Number of web technologies:', len(web_techs))
Number of web technologies: 7
>>> print('Countries:', countries)
Countries: ['United States', 'Canada', 'Mexico', 'Cuba']
>>> print('Number of countries:', len(countries))
Number of countries: 4
```

- Lists can have items of different data types:

```
>>> lst=['Asabeneh', 250, True, {'country':'Finland', 'city':'Helinski'}] #list containing different data types
>>> print(lst)
['Asabeneh', 250, True, {'country': 'Finland', 'city': 'Helinski'}]
```

## Accessing List Items using positive indexing

- We access each item in a list using their index. A list index starts from 0. The picture below shows clearly where the index starts. 
lst=['banana','orange','mango','lemon']
lst = 0, 1, 2, 3

```
>>> second_fruit=fruits[1]
>>> print(second_fruit)
orange
>>> last_fruit=fruits[3]
>>> print(last_fruit)
lemon
>>> last_index=len(fruits) -1
>>> last_fruit=fruits[last_index]
>>> print(last_fruit)
lemon
```

## Accessing List Item using negative indexing

lst=['banana','orange','mango','lemon']
lst = -4, -3, -2, -1

```
>>> fruits=['banana','orange','mango','lemon']
>>> first_fruit= fruits[-4]
>>> last_fruit=fruits[-1]
>>> second_last=fruits[-2]

>>> print(first_fruit)
banana
>>> print(last_fruit)
lemon
>>> print(second_last)
mango
```

## Unpacking list items

```
>>> lst=['item1','item2','item3','item4', 'item5']
>>> first_item, second_item, third_item, *rest=lst
>>> print(first_fruit)
banana
>>> print(second_fruit)
orange
>>> print(third_item)
item3
>>> print(rest)
['item4', 'item5']
```

```
>>> fruits = ['banana','orange', 'mango', 'lemon', 'lime', 'apple']
>>> first_fruit, second_fruit, third_fruit, *rest=fruits
>>> print(first_fruit)
banana
>>> print(second_fruit)
orange
>>> print(third_fruit)
mango
>>> print(rest)
['lemon', 'lime', 'apple']
```

```
>>> #Second Example about unpacking list
>>> first, second, third, *rest, tenth=[1,2,3,4,5,6,7,8,9,10]
>>> print(first)
1
>>> print(second)
2
>>> print(third)
3
>>> print(rest)
[4, 5, 6, 7, 8, 9]
>>> print(tenth)
10
```

```
>>> #Third Example about unpacking list
>>> countries = ['Germany','France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
>>> gr, fr, bg, sw, *scandic, es = countries 
>>> print(gr)
Germany
>>> print(fr) 
France
>>> print(bg)
Belgium
>>> print(sw)
Sweden
>>> print(scandic)
['Denmark', 'Finland', 'Norway', 'Iceland']
>>> print(es)
Estonia
```

## Slicing items from a list

- Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list. 
(default values for start = 0, end=len(lst))

```
>>> fruits=['banana','orange','mango','lemon']
>>> all_fruits=fruits[-4:]
>>> orange_and_mango=fruits[-3:-1]
>>> orange_mango_lemon=fruits[-3:] #this will give starting from -3 to the end 
>>> reverse_fruits=fruits[::-1] #a negative step will take the list in reverse order
>>> print(fruits)
['banana', 'orange', 'mango', 'lemon']
>>> print(all_fruits)
['banana', 'orange', 'mango', 'lemon']
>>> print(orange_and_mango)
['orange', 'mango']
>>> print(orange_mango_lemon)
['orange', 'mango', 'lemon']
>>> print(reverse_fruits)
['lemon', 'mango', 'orange', 'banana']
```

## Modifying lists

- Lists are mutable(modifiable) Modify the fruit list. 
    - Modify a list by casting a list var, specifying the index of the var and then casting it a different value

```
>>> fruits=['banana','orange','mango','lemon']
>>> fruits[0]='avocado'
>>> print(fruits)
['avocado', 'orange', 'mango', 'lemon']
>>> fruits[1]='apple'
>>> print(fruits)
['avocado', 'apple', 'mango', 'lemon']
>>> last_index=len(fruits)-1
>>> fruits[last_index]='lime'
>>> print(fruits)
['avocado', 'apple', 'mango', 'lime']
```

## Checking items in a list

- Check if an item is in a list using the in operator. 
    - Returns a boolean (True/False)

```
>>> fruits=['banana','orange','mango','lemon']
>>> does_exist = 'banana' in fruits
>>> print(does_exist)
True
>>> does_exist='lime' in fruits
>>> print(does_exist)
False
```

## Adding items in a list

- To add item to the end of an existing list we use the method append()

```
>>> #syntax
>>> lst=list()
>>> lst.append('item') 
>>> print(lst)        
['item']
```

## Inserting items into a list 

- Use the insert() method to insert a single item at specified index in list. Other items are shifted to the right
- Insert method takes two arguments: index & item to insert. 

```
>>> lst=['item1','item2']
>>> # lst.insert(index, item)
>>> fruits=['banana','orange','mango','lemon']
>>> fruits.insert(2, 'apple')
>>> print(fruits)
['banana', 'orange', 'apple', 'mango', 'lemon']
>>> fruits.insert(3, 'lime')
>>> print(fruits)
['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
```

## Removing items from a list

- Remove method removes item from a list

General syntax
```
#syntax
lst=['item1','item2']
lst.remove(item)
```

Examples with fruits 
```
>>> fruits=['banana','orange','mango','lemon']
>>> fruits.remove('banana')
>>> print(fruits)
['orange', 'mango', 'lemon']
>>> fruits.remove('lemon')
>>> print(fruits)
['orange', 'mango']
```

## Removing items using pop

- pop() method removes specified index, (or last item if index is not specified)

General syntax
```
lst=['item1','item2']
lst.pop() #last item
lst.pop(index)
```

```
>>> fruits=['banana','orange','mango','lemon']
>>> fruits.pop()
'lemon'
>>> print(fruits)
['banana', 'orange', 'mango']
>>> fruits.pop(0)
'banana'
>>> print(fruits)
['orange', 'mango']
```

## Removing items using del

- del keyword removes specified index; deletes items within index range; deletes the entire list completely also. 

```
#Syntax
lst=['item1','item2']
del lst[index] #delete only a single item from the list
del lst #delete the list completely
```

Examples:
```
>>> fruits=['banana','orange','mango','lemon']
>>> del fruits[0]
>>> print(fruits)
['orange', 'mango', 'lemon']
>>> del fruits[1]
>>> print(fruits)
['orange', 'lemon']
>>> fruits=['banana','orange','mango','lemon','kiwi','lime']
>>> del fruits[1:3]
>>> print(fruits)
['banana', 'lemon', 'kiwi', 'lime']
>>> del fruits
>>> print(fruits)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruits' is not defined
```

## Clearing list items
- clear() method empties the list 

```
#Syntax
lst=['item1','item2']
lst.clear()
```

Examples:
```
>>> fruits=['banana','mango','orange','lemon']
>>> print(fruits)
['banana', 'mango', 'orange', 'lemon']
>>> fruits.clear()
>>> print(fruits)
[]
```

## Copying a list

- Possible to make a copy of a list and assign it to a new variable; list1=list2 for example
    - The issue here is any changes made in one list carry over to the other one. 
    - To avoid this, we can use copy()

```
#Syntax
lst=['item1','item2']
lst_copy=lst.copy()
```

Examples
```
>>> fruits=['banana','orange','lemon','mango']
>>> fruits_copy=fruits.copy() 
>>> print(fruits_copy)
['banana', 'orange', 'lemon', 'mango']
```

## Joining lists

- Several ways to join(concatenate) two or more lists in python.

1. Plus Operator (+)

```
#Syntax
list3=list1 + list2
```
Example:
```
>>> positive=[1,2,3,4,5]
>>> zero=[0]
>>> negative_numbers=[-5,-4,-3,-2,-1]
>>> integers = negative_numbers + zero + positive
>>> print(integers)
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
>>> fruits=['banana','orange','mango','lemon']
>>> vegetables=['Tomato','Potato','Cabbage','Onion','Carrot']
>>> fruits_and_vegetables= fruits + vegetables
>>> print(fruits_and_vegetables)
['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

2. extend() method; allows you to append items in a list 

```
#syntax
list1=['item1', 'item2']
list2=['item3','item4']
list1.extend(list2)
```

Examples:

```
>>> num1=[0,1,2,3]
>>> num2=[4,5,6]
>>> num1.extend(num2)
>>> print('Numbers:', num1)
Numbers: [0, 1, 2, 3, 4, 5, 6]
>>> negative_numbers=[-5,-4,-3,-2,-1]
>>> zero=[0]
>>> positive_numbers=[1,2,3,4,5]
>>> negative_numbers.extend(zero)
>>> negative_numbers.extend(positive_numbers)
>>> print('Integers:', negative_numbers)
Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
>>> fruits=['banana','orange','mango','lemon']
>>> vegetables=['Tomato','Potato','Cabbage','Onion','Carrot']
>>> fruits.extend(vegetables)
>>> print('Fruits and vegetables:', fruits)
Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

## Counting items in a list

- count() returns the number of times an item appears in a string 

```
lst=['item1','item2']
lst.count(item)
```

Examples;
```
>>> fruits=['banana','orange','mango','lemon']
>>> print(fruits.count('orange')) 
1
>>> ages=[22,19,24,25,26,24,25,24]
>>> print(ages.count(24))
3
```

## Finding index of an item

- index() returns the index of an item in a list

Syntax:
```
lst=['item1','item2']
lst.index(item)
```

Example:
```
>>> fruits=['banana','orange','mango','lemon']
>>> print(fruits.index('lemon'))
3
>>> ages=[22,24,22,24,26,24,25,24]
>>> print(ages.index(24))
1
```
## Reversing a List

- reverse() reverses the order of a list 

General syntax:
```
lst=['item1','item2']
lst.reverse()
```

Examples:
```
>>> fruits=['banana','orange','mango','lemon']
>>> fruits.reverse()
>>> print(fruits)
['lemon', 'mango', 'orange', 'banana']
>>> ages=[22,19,24,25,26,24,25,24]
>>> ages.reverse()
>>> print(ages)
[24, 25, 24, 26, 25, 24, 19, 22]
```

## Sorting List Items

- You can sort lists with sort() method  and sorted() built-in-functions
    - sort() reorders list in ascending order, modifies the original list.
        - sort() argument; reverse=true, arrange list in descending order

sort()

```
#Syntax
lst=['item1','item2']
lst.sort()
lst.sort(reverse=True)
```

Example:
```
>>> fruits=['banana','orange','mango','lemon']
>>> fruits.sort()
>>> print(fruits)
['banana', 'lemon', 'mango', 'orange']
>>> fruits.sort(reverse=True)
>>> print(fruits)
['orange', 'mango', 'lemon', 'banana']
>>> ages=[22,19,24,25,26,24,25,26]
>>> ages.sort()
>>> print(ages)
[19, 22, 24, 24, 25, 25, 26, 26]
>>> ages.sort(reverse=True)
>>> print(ages)
[26, 26, 25, 25, 24, 24, 22, 19]
```

sorted():

returns ordered list without modifying original list

```
>>> fruits=['banana','orange','mango','lemon']
>>> print(sorted(fruits))
['banana', 'lemon', 'mango', 'orange']
>>> fruits=sorted(fruits,reverse=True)
>>> print(fruits)
['orange', 'mango', 'lemon', 'banana']
```