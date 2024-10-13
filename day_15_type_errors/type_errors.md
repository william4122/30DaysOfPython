# Python Error Types

*Further reading: https://docs.python.org/3/library/exceptions.html#built-in-exceptions*

- Writing code you are going to have a typo or something like that. When that happens python will actually give you some feedback on where the problem is in your code and what kind of problem it is

- Knowing the different error types helps you with debugging your code

- Lets look at the most common errors

## SyntaxError

### Example 1: SyntaxError

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world
  File "<stdin>", line 1
    print 'hello world
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print('hello world')
hello world
```

- This is a syntax error because we did not close the string

## NameError

- This error meant you have not declared a variable that you are calling

### Example 1: NameError

```
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age=26
>>> print(age)
26
```

- We fix this error in python bvy declaring the variable and assigning a value to it that the name error referenced.

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> age=26
>>> print(age)
26
```

- *The type of error was a NameError. We debugged the error by defining the variable name.*

## IndexError

### Example 1: IndexError

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1,2,3,4,5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

- We tried to access an item in the list that is not in the range of items in the list. So an index error gets thrown

- How could we address this error? 
    - Either we add more items to the list so the index we try to access is not out of range. Or we access an index within the range of the list

```
#adding more items to the list
>>> numbers = [1,2,3,4,5,6] 
>>> numbers[5]
6

#accessing a index within range
>>> numbers = [1,2,3,4,5]
>>> numbers[4] 
5
```

## ModuleNotFoundError

- Sounds like an error when you try to use functions within a module you have not imported yet 
    - Lol actually the example we used was you tried to import a module that did not exist aka maths. 

- Possible fixes sound like: don't import the module, or import the module 

### Example 1: ModuleNotFoundError

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
```

- Fix: Import the module 

- What are some functions of the module you could use?
    - We can always figure that out with the dir(module_name) cmd 


```
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']
```

## AttributeError 

- trying to call a function that does not exist in that module
- debug: call the correct function, check your imports 

### Example 1: AttributeError

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
```

- We tried to call a function that does not exist in the math module. PI does not exist so it will throw an attribute error

- If we want to fix this we would address this by referencing the right function in the module math.pi

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
```

## KeyError

- We referenced a key in our users dictionary which did not exist. 
- Debug: Either create the key in the dictionary, or reference the correct key if its due to a typo

### Example 1: KeyError

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Will','age':'26','country':'USA'}
>>> users['name']
'Will'
#here you can see we reference the wrong key: county
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
#here we reference the right key country and can access its value 
>>> users['country'] 
'USA'
```

## TypeError

### Example 1: TypeError

- Sounds like this error gets raised when you are doing something you should not do with a particular data type i.e (adding a number to a string)

```
PS C:\Githubs\30DaysOfPython> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

- To debug these: You need to cast one of the data types so they could be similar 
- Use some common sense though; in our first example, it would not make sense to convert 4 to a string to do string addition, we would get 43
    - In reality, we wanted integer addition so best to convert 3 into a integer and then do addition that way

```
>>> 4 + int('3')
7
```

## ImportError

### Example 1: ImportError

```
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
```

- There is no function in the math module called power, there is one called pow though 

```
>>> from math import pow
>>> pow(2,3)
8.0
```

## ValueError

```
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
```

- You can't change a string to a number

## ZeroDivisionError

```
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

- You can't divide by 0. In math as well as in Python. 


