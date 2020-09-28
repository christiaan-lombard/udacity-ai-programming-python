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