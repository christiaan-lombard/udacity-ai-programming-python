# Python Refresher

- Python is case sensitive
- Python is sensitive to indentation
  - Indented code indicates inner-block
  - Indentation must be consistent
  - Standard indentation is 4 spaces

 - [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)


## Variables


### Types

| Type | Literals |
|---|---|
| `int` | `100` |
| `float` | `1.2, .81, 5.` |
| `bool` | `True, False` |
| `string` | `'Hello', "World", """!"""` |
| `tuple` | `(1200, 600)` |
| `list` | `[1,2,3]` |

- Get type: `type(var)` => `<class 'int'>`
- Explicitly cast types: `int(var)`, `float(var)`,  `string(var)`, `bool(var)`


### Assignment

- Single assignment: `x = 10`
- Multiple assignments: `x, y, z = 10, 6, 100`

Assignment Operators:

| Operator | Example | Equivalent to |
|---|---|---|
| `=` | `x = 5` | `x = 5` |
| `+=` | `x += 5` | `x = x + 5` |
| `-=` | `x -= 5` | `x = x - 5` |
| `*=` | `x *= 5` | `x = x * 5` |
| `/=` | `x /= 5` | `x = x / 5` |
| `%=` | `x %= 5` | `x = x % 5` |
| `//=` | `x //= 5` | `x = x // 5` |
| `**=` | `x **= 5` | `x = x ** 5` |
| `&=` | `x &= 5` | `x = x & 5` |
| `|=` | `x |= 5` | `x = x | 5` |
| `^=` | `x ^= 5` | `x = x ^ 5` |
| `>>=` | `x >>= 5` | `x = x >> 5` |
| `<<=` | `x <<= 5` | `x = x << 5` |


## Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod
- `**` Exponentiation
- `//` Divides and rounds down to the nearest integer

See [Order of Operations](http://mathforum.org/dr.math/faq/faq.order.operations.html)


### Comparison Operators

| Symbol | Operation |
|---|---|
| `<` | Less Than |
| `>` | Greater Than |
| `<=` | Less Than or Equal To |
| `>=` | Greater Than or Equal To |
| `==` | Equal To |
| `!=` | Not Equal To |


### Logical Operators

| Symbol | Operation |
|---|---|
| `and` | Evaluates if all provided statements are True |
| `or` | Evaluates if at least one of many statements is True |
| `not` | Flips the Bool Value |


## Strings

Immutable ordered sequence of characters.

- Declare literals with either single quotes `'` or double quotes `"`
- Escape chars with `\`, eg. `\"`
- Get the length of string with `len(first_word)`


### String Operators

| Operator | Description | Example |
|---|---|---|
| `+` | Concatenation - Adds values on either side of the operator | `a + b` => `'HelloPython'` |
| `*` | Repetition - Creates new strings, concatenating multiple copies of the same string | `a*2` => `'HelloHello'` |
| `[]` | Slice - Gives the character from the given index | `a[1]` => `'e'` |
| `[ : ]` | Range Slice - Gives the characters from the given range | `a[1:4]` => `'ell'` |
| `in` | Membership - Returns true if a character exists in the given string | `'H' in a` => `True` |
| `not in` | Membership - Returns true if a character does not exist in the given string | `'M' not in a` => `True` |
| `r/R` | Raw String - Suppresses actual meaning of Escape characters. The syntax for raw strings is exactly the same as for normal strings with the exception of the raw string operator, the letter "r," which precedes the quotation marks. The "r" can be lowercase (r) or uppercase (R) and must be placed immediately preceding the first quote mark. | `print r'\n'` => `'\n'` and `print R'\n'` prints `'\n'` |
| `%` | Format - Performs String formatting | See [String Formatting Operator](https://python-reference.readthedocs.io/en/latest/docs/str/formatting.html) |


### Common String Methods

> Note: All string methods returns new values. They do not change the original string.

 - `capitalize()` - Converts the first character to upper case
 - `casefold()` - Converts string into lower case
 - `center()` - Returns a centered string
 - `count()` - Returns the number of times a specified value occurs in a string
 - `encode()` - Returns an encoded version of the string
 - `endswith()` - Returns true if the string ends with the specified value
 - `expandtabs()` - Sets the tab size of the string
 - `find()` - Searches the string for a specified value and returns the position of where it was found
 - `format()` - Formats specified values in a string
 - `format_map()` - Formats specified values in a string
 - `index()` - Searches the string for a specified value and returns the position of where it was found
 - `isalnum()` - Returns True if all characters in the string are alphanumeric
 - `isalpha()` - Returns True if all characters in the string are in the alphabet
 - `isdecimal()` - Returns True if all characters in the string are decimals
 - `isdigit()` - Returns True if all characters in the string are digits
 - `isidentifier()` - Returns True if the string is an identifier
 - `islower()` - Returns True if all characters in the string are lower case
 - `isnumeric()` - Returns True if all characters in the string are numeric
 - `isprintable()` - Returns True if all characters in the string are printable
 - `isspace()` - Returns True if all characters in the string are whitespaces
 - `istitle()` - Returns True if the string follows the rules of a title
 - `isupper()` - Returns True if all characters in the string are upper case
 - `join()` - Joins the elements of an iterable to the end of the string
 - `ljust()` - Returns a left justified version of the string
 - `lower()` - Converts a string into lower case
 - `lstrip()` - Returns a left trim version of the string
 - `maketrans()` - Returns a translation table to be used in translations
 - `partition()` - Returns a tuple where the string is parted into three parts
 - `replace()` - Returns a string where a specified value is replaced with a specified value
 - `rfind()` - Searches the string for a specified value and returns the last position of where it was found
 - `rindex()` - Searches the string for a specified value and returns the last position of where it was found
 - `rjust()` - Returns a right justified version of the string
 - `rpartition()` - Returns a tuple where the string is parted into three parts
 - `rsplit()` - Splits the string at the specified separator, and returns a list
 - `rstrip()` - Returns a right trim version of the string
 - `split()` - Splits the string at the specified separator, and returns a list
 - `splitlines()` - Splits the string at line breaks and returns a list
 - `startswith()` - Returns true if the string starts with the specified value
 - `strip()` - Returns a trimmed version of the string
 - `swapcase()` - Swaps cases, lower case becomes upper case and vice versa
 - `title()` - Converts the first character of each word to upper case
 - `translate()` - Returns a translated string
 - `upper()` - Converts a string into upper case
 - `zfill()` - Fills the string with a specified number of 0 values at the beginning


## Collections

### Collection Functions

- `len(coll)` - returns how many elements are in a list.
- `max(coll)` - returns the greatest element of the list. How the greatest element is determined depends on what type objects are in the list. The maximum element in a list of numbers is the largest number. The maximum elements in a list of strings is element that would occur last if the list were sorted alphabetically. This works because the the max function is defined in terms of the greater than comparison operator. The max function is undefined for lists that contain elements from different, incomparable types.
- `min(coll)` - returns the smallest element in a list. min is the opposite of max, which returns the largest element in a list.
- `sorted(coll)` - returns a copy of a list in order from smallest to largest, leaving the list unchanged.

#### Zip

- `zip(list, list, ...)` - zip returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elements in that position from all the iterables.
  - `zip(['a', 'b', 'c'], [1, 2, 3])` => `(('a', 1), ('b', 2), ('c', 3))`
  - Use to iterate lists: `for letter, num in zip(['a', 'b', 'c'], [1, 2, 3]):`
- `zip(*list)` - unzips a list into tuples
  - `letters, nums = zip(*(('a', 1), ('b', 2), ('c', 3)))`
  - `letters` => `['a', 'b', 'c']`, `nums` => `[1, 2, 3]`


#### Enumerate

- `enumerate(list)` -  returns an iterator of tuples containing indices and values of a list.
  - `enumerate(['a', 'b', 'c'])` => `((0, 'a'), (1, 'b'), (2, 'c'))`


### List Comprehension

List comprehensions allow us to create a list using a for loop in one step:
`[{statement} for {element} in {collection}]`

eg. `capitalized_cities = [city.title() for city in cities]`

Add conditionals:

`[{statement} for {element} in {collection} if {condition}]`

eg. `squares = [x**2 for x in range(9) if x % 2 == 0]`

If you would like to add else, you have to move the conditionals to the beginning of the listcomp, right after the expression.

`[{statement} if {condition} else {alernative} for {element} in {collection}]`

eg. `squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]`

## Lists

Mutable ordered sequence of data/elements.

- Assign list: `months = ['Jan', 'Feb', 'Mar', 'Apr', ...]` or `months = list()`
- Access by index: `months[0]` => `'Jan'`
- Access from the end: `months[-1]` => `'Dec'`
- Mutate a value: `months[11] = 'Des'`
- Mutate a slice: `months[3:4] = ['Apr', 'May']`
- Access a subsequence/slice: `months[0:2]` or `months[:2]` => `['Jan', 'Feb']`
- Supports `in` and `not in` operators: `'Jan' in months` => `True`

Other usefull list operations:

- `string.join(list)` - join is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string. `"-".join(["INV", "123"])` => `'INV-123'`


### List methods

- `append()` - Adds an element at the end of the list
- `clear()` - Removes all the elements from the list
- `copy()` - Returns a copy of the list
- `count()` - Returns the number of elements with the specified value
- `extend()` - Add the elements of a list (or any iterable), to the end of the current list
- `index()` - Returns the index of the first element with the specified value
- `insert()` - Adds an element at the specified position
- `pop()` - Removes the element at the specified position
- `remove()` - Removes the first item with the specified value
- `reverse()` - Reverses the order of the list
- `sort()` - Sorts the list


## Tuples

Immutable ordered sequence of data/elements.

- Assign tuple: `dims = (1200, 600, 32)` (brackets optional) or `dims = tuple()`
- Unpack tuple: `length, width, depth = dims`
- Supports all non-mutating list operators


## Sets

Immutable unordered, unique set of data/elements.

- Assign a set: `thisset = set()` or `thisset = {"apple", "banana", "cherry"}`
- Assign a set from a list: `nums = set([1,2,3,4,4])`
- Supports `in` and `not in` operator
- Does not support access by index, slicing

> * You can use curly braces to define a set like this: {1, 2, 3}. However, if you leave the curly braces empty like this: {} Python will instead create an empty dictionary. So to create an empty set, use set().

### Set methods

 - `add()` - Adds an element to the set
 - `clear()` - Removes all the elements from the set
 - `copy()` - Returns a copy of the set
 - `difference()` - Returns a set containing the difference between two or more sets
 - `difference_update()` - Removes the items in this set that are also included in another, specified set
 - `discard()` - Remove the specified item
 - `intersection()` - Returns a set, that is the intersection of two other sets
 - `intersection_update()` - Removes the items in this set that are not present in other, specified set(s)
 - `isdisjoint()` - Returns whether two sets have a intersection or not
 - `issubset()` - Returns whether another set contains this set or not
 - `issuperset()` - Returns whether this set contains another set or not
 - `pop()` - Removes an element from the set
 - `remove()` - Removes the specified element
 - `symmetric_difference()` - Returns a set with the symmetric differences of two sets
 - `symmetric_difference_update()` - inserts the symmetric differences from this set and another
 - `union()` - Return a set containing the union of sets
 - `update()` - Update the set with the union of this set and others


 ## Dictionaries

Maps data in key-value pairs.

- Assign a dictionary: `elements = {'hydrogen': 1, 'helium': 2}` or `elements = dict()`
- Get a value from dictionary: `element1 = elements['hydrogen']`
- Get a value without throwing error: `element1 = elements.get('hydrogen')`
- A dictionary itself is mutable, but each of its individual keys must be immutable.

### Dictionary methods

 - `clear()` - Removes all the elements from the dictionary
 - `copy()` - Returns a copy of the dictionary
 - `fromkeys()` - Returns a dictionary with the specified keys and value
 - `get()` - Returns the value of the specified key
 - `items()` - Returns a list containing a tuple for each key value pair
 - `keys()` - Returns a list containing the dictionary's keys
 - `pop()` - Removes the element with the specified key
 - `popitem()` - Removes the last inserted key-value pair
 - `setdefault(key, value)` - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
 - `update()` - Updates the dictionary with the specified key-value pairs
 - `values()` - Returns a list of all the values in the dictionary


## Control Structures


### If Statement

```py
if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
else:
    print('unrecognized season')
```

Shorthand
```py
x = 10 if a > b else 11
```

### Falsy Values

Here are most of the built-in objects that are considered False in Python:

- constants defined to be false: `None` and `False`
- zero of any numeric type: `0, 0.0, 0j, Decimal(0), Fraction(0, 1)`
- empty sequences and collections: `"", (), [], {}, set(), range(0)`


### For Loops

`for` loops are ideal when the **number of iterations is known or finite**.

- Iterate a collection (list, string, set, tuple, dictionary): `for value in values:`
- Iterate a definite number of times: `for i in range(start,end,increment):`
- Iterate map: `for key, value in map.items():`
- Iterate array with index: `for i, value in enumerate(array):`
- `break` terminates a loop
- `continue` skips one iteration of a loop


### While Loops

`while` loops are ideal when the **iterations need to continue until a condition is met**.

 - Loop while condition met: `while num < end_num:`
 - Supports `break` and `continue`


## Functions

```py

# function definition
def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

```

 - If there is no return statement, the function returns `None`.
 - Arguments are optional if default is supplied
 - Arguments can be passed by name `cylinder_volume(radius=2,height=5)`
 - Variables declared inside a function is scoped to the function body.
 - Variables **outside** the function can be accessed but **not modified** (throws `UnboundLocalError`).


### Lambda Expression

```py
double = lambda x: x * 2
```


## Iterators and Generators

*Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.* - [Stack Overflow](https://softwareengineering.stackexchange.com/questions/290231/when-should-i-use-a-generator-and-when-a-list-in-python/290235)

```py
def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1
```

See [Python docs - Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)


## Errors and Exceptions

- **Syntax errors** occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.

- **Exceptions** occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.

### Common Exceptions

- `KeyError` - Raised when a mapping (dictionary) key is not found in the set of existing keys.
- `AssertionError` - Raised when an assert statement fails.
- `IndexError` - Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)
- `ValueError` - Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.
- `TypeError` - Raised when an operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.
- `ZeroDivisionError` - Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.

[See built-in exceptions](https://docs.python.org/3/library/exceptions.html)

### Try Except

```py
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

finally:
  # execute regardless of exception

```

### Raise Exception

```py
raise ValueError("That is not a positive number!")
```


## Working with Files

### File Modes
- `r` - Read - Default value. Opens a file for reading, error if the file does not exist
- `a` - Append - Opens a file for appending, creates the file if it does not exist
- `w` - Write - Opens a file for writing, creates the file if it does not exist
- `x` - Create - Creates the specified file, returns an error if the file exists

Additional flags:
- `t` - Text - Default value. Text mode
- `b` - Binary - Binary mode (e.g. images)

### Read Files

```py
f = open('my_path/my_file.txt', 'rt')
file_data = f.read()
f.close()
```

### Write Files

```py
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
```

### With

This with keyword allows you to open a file, do operations on it, and automatically close it after the code block is executed.

```py
with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
```


## Import Scripts

`import` followed by the name of the file, without the .py extension.

```py
import useful_functions
useful_functions.add_five([1, 2, 3, 4])

# rename a module
import useful_functions as uf
uf.add_five([1, 2, 3, 4])

# import individual objects from a module
from collections import defaultdict, namedtuple

# import an object from a module and rename it
from module_name import object_name as new_name

# import every object individually from a module (DO NOT DO THIS)
from module_name import *

# import submodule
import package_name.submodule_name
```

### Main Block

When we run a script, Python recognizes this module as the main program, and sets the `__name__` variable for this module to the string `"__main__"`. For any modules that are imported in this script, this built-in `__name__` variable is just set to the name of that module.

To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an `if __name__ == "__main__"` block.

```py
if __name__ == "__main__":
  print('I should not execute if imported')
```

### Common Modules

- `csv`: very convenient for reading and writing csv files
- `collections`: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
- `random`: generates pseudo-random numbers, shuffles sequences randomly and chooses random items
- `string`: more functions on strings. This module also contains useful collections of letters like string.digits (a string containing all characters which are valid digits).
- `re`: pattern-matching in strings via regular expressions
- `math`: some standard mathematical functions
- `os`: interacting with operating systems
- `os.path`: submodule of os for manipulating path names
- `sys`: work directly with the Python interpreter
- `json`: good for reading and writing json files (good for web work)


## Third-Party Libraries

### Install packages

`pip install package_name`

### Using a requirements.txt File

Larger Python programs might depend on dozens of third party packages. To make it easier to share these programs, programmers often list a project's dependencies in a file called requirements.txt:

```
beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
```

You can use pip to install all of a project's dependencies at once by typing `pip install -r requirements.txt` in your command line


### Useful Third-Party Packages

- [**IPython**](https://ipython.org/) - A better interactive Python interpreter
- [**requests**](http://docs.python-requests.org/) - Provides easy to use methods to make web requests. Useful for accessing web APIs.
- [**Flask**](http://flask.pocoo.org/) - a lightweight framework for making web applications and APIs.
- [**Django**](https://www.djangoproject.com/) - A more featureful framework for making web applications. Django is particularly good for designing complex, content heavy, web applications.
- [**Beautiful Soup**](https://www.crummy.com/software/BeautifulSoup/) - Used to parse HTML and extract information from it. Great for web scraping.
- [**pytest**](http://doc.pytest.org/) - extends Python's builtin assertions and unittest module.
- [**PyYAML**](http://pyyaml.org/wiki/PyYAML) - For reading and writing YAML files.
- [**NumPy**](http://www.numpy.org/) - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
- [**pandas**](http://pandas.pydata.org/) - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
- [**matplotlib**](http://matplotlib.org/) - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
- [**ggplot**](http://ggplot.yhathq.com/) - Another 2D plotting library, based on R's ggplot2 library.
- [**Pillow**](https://python-pillow.org/) - The Python Imaging Library adds image processing capabilities to your Python interpreter.
- [**pyglet**](http://www.pyglet.org/) - A cross-platform application framework intended for game development.
- [**Pygame**](http://www.pygame.org/) - A set of Python modules designed for writing games.
- [**pytz**](http://pytz.sourceforge.net/) - World Timezone Definitions for Python


## Object Oriented Programming

- [class methods, instance methods, and static methods](https://realpython.com/instance-class-and-static-methods-demystified/) - these are different types of methods that can be accessed at the class or object level
- [class attributes vs instance attributes](https://www.python-course.eu/python3_class_and_instance_attributes.php) - you can also define attributes at the class level or at the instance level
- [multiple inheritance, mixins](https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556) - A class can inherit from multiple parent classes
- [Python decorators](https://realpython.com/primer-on-python-decorators/) - Decorators are a short-hand way for using functions inside other functions


```py
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def set_full_name(self, first_name, last_name):
        this.first_name = first_name
        this.last_name = last_name

employee = Employee('Christiaan', 'Lombard')

```

- [Python Properties vs. Getters and Setters](https://www.python-course.eu/python3_properties.php)

### Magic Methods

Magic methods are not meant to be invoked directly by you, but the invocation happens internally from the class on a certain action. For example, when you add two numbers using the + operator, internally, the __add__() method will be called. - [Python - Magic Methods](https://www.tutorialsteacher.com/python/magic-methods-in-python)

```py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __add__(self, other):
        return Rectangle(self.width + other.width, self.height + other.height)

    def __repr__(self):
        return 'Rectangle %fx%f' % (self.width, self.height)

```


### Inheritance

```py
class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

class Shirt(Clothing):

    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2*self.price

class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)
```
