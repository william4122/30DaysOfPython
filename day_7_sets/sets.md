# Sets

- Sets are collections of items

- Can apply the mathematical definition here

- Unordered, unindexed distinct elements
    - Used to store unique items
    - possible to find union, intersection, difference, symmetric difference, subset, super set and disjoint set 

## Creating a Set

- You create sets with the set() *built in function*

Create empty set
```
>>> st=set()
>>> print(st)
set()
```
Create set with initial items:
```
>>> st={'item1','item2','item3','item4'}
>>> print(st)
{'item1', 'item2', 'item3', 'item4'}
>>> fruits={'banana','orange','mango','lemon'}
>>> print(fruits)
{'orange', 'mango', 'banana', 'lemon'}
```

## Getting Set's Length

- The len() method gives us the length of a set 

```
>>> st={'item1','item2','item3','item4'}
>>> print(len(st))
4
```

## Accessing Items in a Set

- You can use loops to access items in a set, will be discussed in the Loops section.

## Checking an Item

- You can check if something exists in a list with the in membership operator

```
>>> st={'item1','item2','item3','item4'}
>>> print("Does set st contain item3? ", 'item3' in st)
Does set st contain item3?  True
>>> fruits={'banana', 'orange', 'mango', 'lemon'}
>>> print('mango' in fruits)
True
```

## Adding Items to a Set 

- While you can't change the items in a set, you can add items into a set

- using the add() method [ONE]

```
>>> st={'item1','item2','item3','item4'}
>>> print(st)
{'item5', 'item2', 'item1', 'item4', 'item3'}
>>> fruits={'banana','apple','orange','mango'}
>>> fruits.add('lime')
>>> print(fruits)     
{'banana', 'orange', 'apple', 'mango', 'lime'}
```

- multiple items can be added using update()
    takes a list as an argument 
```
>>> st={'item1','item2','item3','item4'}
>>> st.update(['item5','item6','item7','item8'])
>>> print(st)
{'item5', 'item2', 'item7', 'item8', 'item1', 'item4', 'item6', 'item3'}
>>> fruits={'banana','orange','mango','lemon'}
>>> vegetables=['tomato','potato','cabbage','onion','carrot']
>>> fruits.update(vegetables)
>>> print(fruits)
{'orange', 'banana', 'lemon', 'mango', 'cabbage', 'carrot', 'onion', 'potato', 'tomato'}
```

## Removing Items from a Set

- The remove() method gets rid of an item in a set but raises errors if the item is not found (make sure you check if the item exists in a set)
    - discard() method does not raise any errors 

```
>>> st={'item1','item2','item3','item4'}
>>> st.remove('item5')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'item5'
>>> st.remove('item4') 
>>> print(st)
{'item2', 'item3', 'item1'}
>>> st.discard('item5')
>>> st.discard('item3')
>>> print(st)
{'item2', 'item1'}
```

- pop() removes a random item from the list & returns the removed item
```
>>> fruits={'banana','orange','mango','lemon'}
>>> fruits.pop()
'lemon'
```

## Clearing Items in a Set
- clear method empties a set 
```
>>> #syntax of clear method
>>> st={'item1','item2','item3','item4'}
>>> st.clear()
>>> print(st)
set()
>>> fruits={'banana','orange','lemon','mango'}
>>> fruits.clear()
>>> print(fruits)
set() <- This is what a cleared set looks like
```
## Deleting a Set

- the del operator can be used to delete a set 

```
>>> st={'item1','item2','item3','item4'}
>>> del st
>>> print(st)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'st' is not defined. Did you mean: 'set'?
>>> fruits={'banana','apple','lemon','mango'}
>>> del fruits
>>> print(fruits)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruits' is not defined
```

## Converting List to Set

- You can convert from list -> set and from set -> list 
- Going from list to set removes duplicates. 

```
>>> lst=['item1','item2','item3','item4']
>>> st=set(lst)
>>> print(st)
{'item2', 'item3', 'item1', 'item4'}
>>> fruits=['banana','orange','mango','lemon','orange','banana']
>>> fruits=set(fruits)
>>> print(fruits)
{'lemon', 'mango', 'orange', 'banana'}
```

## Joining Sets

- The union() or update() method joins two sets

- union() returns a new set 

```
>>> st1={'item1','item2','item3','item4'}
>>> st2={'item5','item6','item7','item8'}
>>> st3=st1.union(st2)
>>> print(st3)
{'item5', 'item2', 'item7', 'item8', 'item1', 'item4', 'item6', 'item3'}
>>> fruits={'banana','orange','lemon','mango'}
>>> vegetables={'tomato','potato','cabbage','onion','carrot'}
>>> print(fruits.union(vegetables))
{'orange', 'banana', 'lemon', 'mango', 'cabbage', 'carrot', 'tomato', 'potato', 'onion'}
```
- update: inserts a set into another given set
    - While this may have been taught in the class I am not sure it works because it did not work in the exercises (ask a trusted resource)

```
>>> st1={'item1','item2','item3','item4'}
>>> st2={'item5','item6','item7','item8'}
>>> st1.update(st2)
>>> print(st1)
{'item5', 'item2', 'item7', 'item8', 'item1', 'item4', 'item6', 'item3'}
>>> fruits={'banana','orange','mango','lemon'}
>>> vegetables={'tomato','potato','cabbage','onion','carrot'}
>>> print(fruits.union(vegetables))
{'orange', 'banana', 'lemon', 'mango', 'cabbage', 'carrot', 'tomato', 'potato', 'onion'}
```

## Finding Intersection Items

- Intersection gives you set of items in both sets 

Example:
```
>>> st1={'item1','item4','item3','item4'}
>>> st2={'item3','item2'}
>>> st1.intersection(st2)
{'item3'}
>>> whole_numbers={0,1,2,3,4,5,6,7,8,9,10}
>>> even_numbers={0,2,4,6,8,10}  
>>> whole_numbers.intersection(even_numbers)
{0, 2, 4, 6, 8, 10}
>>> python={'p','y','t','h','o','n'}
>>> dragon={'d','r','a','g','o','n'}
>>> python.intersection(dragon)
{'o', 'n'}
```
## Checking subset and super set

- You are either a subset or super set of other sets

subset: issubset()
superset: issuperset

```
>>> st1={'item1','item2','item3','item4'}
>>> st2={'item2','item3'}
>>> st2.issubset(st1)
True
>>> st1.issuperset(st2)
True
>>> whole_numbers={0,1,2,3,4,5,6,7,8,9,10}
>>> even_numbers={0,2,4,6,8,10}
>>> whole_numbers.issubset(even_numbers)
False
>>> whole_numbers.issuperset(even_numbers)
True
>>> python={'p','y','t','h','o','n'} 
>>> dragon={'d','r','a','g','o','n'} 
>>> python.issubset(dragon)
False
```

## Checking the difference between two sets

Difference between two sets:

```
>>> st1={'item1','item2','item3','item4'}
>>> st2={'item2','item3'}
>>> st2.difference(st1)
set()
>>> st1.difference(st2)
{'item1', 'item4'}
>>> whole_numbers={0,1,2,3,4,5,6,7,8,9,10} 
>>> even_numbers={0,2,4,6,8,10}
>>> whole_numbers.difference(even_numbers)
{1, 3, 5, 7, 9}
>>> dragon={'d','r','a','g','o','n'}
>>> python={'p','y','t','h','o','n'} 
>>> python.difference(dragon)
{'t', 'p', 'h', 'y'}
>>> dragon.difference(python)
{'a', 'r', 'g', 'd'}
```

## Finding symmetric difference between two sets

- Returning the symmetric difference means returning a set thta contains all items from both sets except items that appear in both sets

```
>>> st1={'item1','item2','item3','item4'}
>>> st2={'item2','item3'}
>>> st2.symmetric_difference(st1)
{'item1', 'item4'}
>>> whole_numbers={0,1,2,3,4,5,6,7,8,9,10}
>>> even_numbers={0,2,4,6,8,10}
>>> whole_numbers.symmetric_difference(even_numbers) 
{1, 3, 5, 7, 9}
>>> python={'p','y','t','h','o','n'}
>>> dragon={'d','r','a','g','o','n'} 
>>> python.symmetric_difference(dragon)
{'p', 'd', 't', 'a', 'y', 'g', 'h', 'r'}
```
## Joining sets 

- If two sets don't have a common item they are disjoint sets. Check if two sets are joint/disjoint using isdisjoint()

```
>>> st1={'item1','item2','item3','item4'}
>>> st2={'item2','item3'}
>>> st2.isdisjoint(st1)
False
>>> even_numbers={0,2,4,6,8,10}
>>> odd_numbers={1,3,5,7,9,11}
>>> even_numbers.isdisjoint(odd_numbers)
True
>>> python={'p','y','t','h','o','n'}      
>>> dragon={'d','r','a','g','o','n'}
>>> python.isdisjoint(dragon)
False
```

This was a homework question but I think should be here:
Explain the difference between the following data types: string, list, tuple and set

String = any data that is in text 
List = ordered collection of items, modifiable, allows duplicate members.
Tuple = Ordered collection, not modifiable, allows duplicate members. 
Set = unordered collection, modifiable, no duplicate members. 