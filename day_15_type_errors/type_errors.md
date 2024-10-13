# Python Error Types

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
 