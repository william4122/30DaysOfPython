# Dictionaries

- A dictionary is a collection of unordered, modifiable (mutable), paired (key:value) data types

## Creating a Dictionary

- Create dictionary using curly brackets or with the dict() built-in function

```
>>> #syntax
>>> empty_dict={}
>>> #dictionary with data values
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> print(dct)
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> print(person)
{'first_name': 'Will', 'last_name': 'Rodr', 'age': '260', 'country': 'USA', 'is_married': 'False', 'skills': ['Windows', 'Chemistry', 'Crying', 'Loser'], 'address': {'street': 'Wills world', 'zipcode': '02210'}}
```

## Dictionary length

- When you use the len() on a dct you get the number of key:value pairs in the dictionary

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> print(len(dct))
4
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> print(len(person))
7
```

## Accessing Dictionary Items

- access dictionary items by referring to its key name. 

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> print(dct['key1'])
value1
>>> print(dct['key4'])
value4
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> print(person['first_name'])  
Will
>>> print(person['country'])
USA
>>> print(person['skills'])
['Windows', 'Chemistry', 'Crying', 'Loser']
>>> print(person['skills'][0])
Windows
>>> print(person['address']['street'])
Wills world
>>> print(person['city'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'city'
```

- You see how when we went to access the city key we got an error that it did not exist; if we want to avoid this kind of error we should check if the key exists or use the get method. 
- The get method returns None, which is a NoneType object data type, if key does not exist. 

```
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> print(person.get('first_name'))
Will
>>> print(person.get('country'))
USA
>>> print(person.get('skills'))
['Windows', 'Chemistry', 'Crying', 'Loser']
>>> print(person.get('city'))
None
```

## Adding items to a dictionary

- add new key and value pairs to a dictionary

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> dct['key5']='value5'
>>> print(dct)
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5'}
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> person['job_title']='Premium Support Engineer Level 2'
>>> person['skills'].append('HTML')
>>> print(person)
{'first_name': 'Will', 'last_name': 'Rodr', 'age': '260', 'country': 'USA', 'is_married': 'False', 'skills': ['Windows', 'Chemistry', 'Crying', 'Loser', 'HTML'], 'address': {'street': 'Wills world', 'zipcode': '02210'}, 'job_title': 'Premium Support Engineer Level 2'}
```

## Modifying items in a dictionary

- You can also modify items in a dictionary, simply specify the index of the key and assign it a new value
```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> dct['key1']='value-one'
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> person['first_age']='Eyob'
>>> person['age']=252
>>> print(person)
{'first_name': 'Will', 'last_name': 'Rodr', 'age': 252, 'country': 'USA', 'is_married': 'False', 'skills': ['Windows', 'Chemistry', 'Crying', 'Loser'], 'address': {'street': 'Wills world', 'zipcode': '02210'}, 'first_age': 'Eyob'}
>>> person['first_name']='Eyob' 
>>> print(person)
{'first_name': 'Eyob', 'last_name': 'Rodr', 'age': 252, 'country': 'USA', 'is_married': 'False', 'skills': ['Windows', 'Chemistry', 'Crying', 'Loser'], 'address': {'street': 'Wills world', 'zipcode': '02210'}, 'first_age': 'Eyob'}
```
## Checking keys in a dictionary

- The in operator tells you if a key exists in a dictionary, returns a boolean 

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> print('key2' in dct)
True
>>> print('key5' in dct)
False
```

## Removing Key and Value pairs from a dictionary

- pop(key): remove item with specified key name
- popitem(): remove last item
- del: remove item with specified key name

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
# using pop to delete a specific index 
>>> dct.pop('key1') 
'value1'
# using popitem to delete the last item
>>> dct.popitem()
('key4', 'value4')
>>> del dct['key2']
# using del
>>> print(dct)
{'key3': 'value3'}
>>> person={'first_name':'Will','last_name':'Rodr','age':'260','country':'USA','is_married':'False','skills':['Windows','Chemistry','Crying','Loser'],'address':{'street':'Wills world','zipcode':'02210'}}
>>> person.pop('first_name')
'Will'
>>> person.popitem()
('address', {'street': 'Wills world', 'zipcode': '02210'})
>>> del person['is_married']
>>> print(person)
{'last_name': 'Rodr', 'age': '260', 'country': 'USA', 'skills': ['Windows', 'Chemistry', 'Crying', 'Loser']}
```

## Changing Dictionary to a List of Items

- items() method changes a dictionary to a list of tuples
```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> print(dct.items())
dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```
## Clearing a Dictionary
- Remove all items in a dictionary

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> print(dct.clear())
None
```
## Deleting a Dictionary

- Delete a dictionary completely using del 

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> del dct
>>> print(dct)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dct' is not defined. Did you mean: 'oct'?
```

## Copy a Dictionary

- the copy() method will allow you o copy a dictionary while avoiding mutation of the original dictionary 

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> dct_copy=dct.copy()
>>> print(dct_copy)
{'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
```

## Getting Dictionary Keys as a List

- The keys() method gives us all the keys in a dictionary as a list


```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> keys=dct.keys()
>>> print(keys)
dict_keys(['key1', 'key2', 'key3', 'key4'])
```

## Getting Dictionary Values as a List 

- The values method gives all the values in the dictionary as a list:

```
>>> dct={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
>>> values=dct.values()
>>> print(values)
dict_values(['value1', 'value2', 'value3', 'value4'])
```
