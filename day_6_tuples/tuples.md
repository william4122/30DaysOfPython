# Tuples

- Tuples are collections of data type which are ordered/unchangeable(immutable)

- Tuples are written with round brackets (), remember a list was with []

- You CANNOT change the values of a tuple once you make it 
    - No add, insert, remove methods because they are not modifiable

### Methods tuples can use:
- tuple(): create empty tuple
- count(): count specified item in tuple
- index(): find index of specified item in tuple
    - operator: to join two or more tuples and to create a new tuple

## Creating a tuple

- Empty tuple: creating an empty tuple

```
>>> #empty tuple syntax
>>> empty_tuple=tuple()
```

- Tuple with values

```
>>> #tyuple with values
>>> tpl=('Adidas','Nike','Sketcher')
>>> fruits=('banana','orange','mango','lemon') 
```

## Tuple length

- the len() method gets you the length of a tuple

```
>>> tpl=('item1','item2','item3')              
>>> len(tpl)
3
```
## Accessing Tuple Items

- Same kind of behavior as with lists
    - Positive indexing:
    ```
    >>> tpl=('item1','item2','item3')
    >>> first_item=tpl[0]
    >>> second_item=tpl[1] 
    >>> fruits=('banana','orange','mango','lemon')
    >>> first_fruit=fruits[0]
    >>> second_fruit=fruits[1]
    >>> last_index=len(fruits)-1
    >>> last_fruit=fruits[last_index]
    ```
    - Negative indexing:
        - Starting from the end -1, and then going more negative

    ```
    >>> tpl=('item1','item2','item3')
    >>> first_item=tpl[-3]
    >>> second_item=fruits[-2] 
    >>> second_item=tpl[-2] 
    >>> fruits=('banana','orange','mango','lemon')
    >>> first_fruit=fruits[-4]
    >>> second_fruit=fruits[-3]
    >>> last_fruit=fruits[-1]
    ```

## Slicing Tuples

- Slice out sub-tuple by specifying range of indexes to start/end in the tuple; return value will be a new tuple. 

- Range of positive indexes:
```
>>> tpl=('item1','item2','item3','item4')
>>> all_items=tpl[0:4]
>>> all_items=tpl[0:]
>>> print(all_items)
('item1', 'item2', 'item3', 'item4')
>>> middle_two_items=tpl[1:3]
>>> print(middle_two_items)
('item2', 'item3')
>>> fruits=('banana','orange','mango','lemon')
>>> all_fruits=fruits[0:4]
>>> print(all_fruits)
('banana', 'orange', 'mango', 'lemon')
>>> all_fruits=fruits[0:]
>>> print(all_fruits)
('banana', 'orange', 'mango', 'lemon')
>>> orange_mango=fruits[1:3]
>>> print(orange_mango)
('orange', 'mango')
>>> orange_to_the_rest=fruits[1:]
>>> print(orange_to_the_rest)
('orange', 'mango', 'lemon')
```

- Range of negative indexes:

```
>>> tpl=('item1','item2','item3','item4') 
>>> all_items=tpl[-4:]
>>> print(all_items)
('item1', 'item2', 'item3', 'item4')
>>> middle_two_items=tpl[-3:-1]
>>> print(middle_two_items)
('item2', 'item3')
>>> fruits=('banana','orange','mango','lemon')
>>> all_fruits=fruits[-4:]
>>> print(all_fruits)
('banana', 'orange', 'mango', 'lemon')
>>> orange_mango=fruits[-3:-1]
>>> print(orange_mango) 
('orange', 'mango')
>>> orange_to_the_rest=fruits[-3:]
>>> print(orange_to_the_rest)
('orange', 'mango', 'lemon')
```

## Changing Tuples to lists

- Just like anything else, we can convert from tuples -> lists and also backwards as well 

```
>>> tpl=('item1','item2','item3','item4')
>>> lst=list(tpl)
>>> print(lst)
['item1', 'item2', 'item3', 'item4']
>>> fruits=('banana','orange','mango','lemon')
>>> fruits=list(fruits)
>>> print(fruits)
['banana', 'orange', 'mango', 'lemon']
>>> fruits=tuple(fruits)
>>> print(fruits)
('banana', 'orange', 'mango', 'lemon')
```

## Checking an item in a Tuple

- Use the in operator to check if something exists in a tuple, returns a boolean 

```
>>> tpl=('item1','item2','item3','item4')
>>> 'item2' in tpl
True
>>> fruits=('banana','orange','mango','lemon')
>>> print('orange' in fruits)
True
>>> print('apple' in fruits)
False
>>> fruits[0]='apple'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

## Joining Tuples

- Join two or more tuples together with the + operator

```
>>> tpl1=('item1','item2','item3')
>>> tpl2=('item4','item5','item6')
>>> tpl3=tpl1 + tpl2
>>> print(tpl3)
('item1', 'item2', 'item3', 'item4', 'item5', 'item6')
```

## Deleting Tuples 
- Not possible to remove a single item in a tuple, but possible to delete a whole tuple using del 

```
>>> tpl1=('item1','item2','item3')
>>> del tpl1
>>> print(tpl1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tpl1' is not defined. Did you mean: 'tpl'?
>>> fruits=('banana','orange','mango','lemon')
>>> del fruits
>>> print(fruits)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'fruits' is not defined
```
