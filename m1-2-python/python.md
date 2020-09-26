# Python Refresher

 - [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/)


## Arithmetic Operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod
- `**` Exponentiation
- `//` Divides and rounds down to the nearest integer

See [Order of Operations](http://mathforum.org/dr.math/faq/faq.order.operations.html)


## Variables


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


### Types

| Type | Literals |
|---|---|
| `int` | `100` |
| `float` | `1.2, .81, 5.` |
| `bool` | `True, False` |
| `string` | `'Hello', "World", """!"""` |


- Get type: `type(var)` => `<class 'int'>`
- Explicitly cast types: `int(var)`, `float(var)`,  `string(var)`, `bool(var)`


## Comparison Operators

| Symbol | Operation |
|---|---|
| `<` | Less Than |
| `>` | Greater Than |
| `<=` | Less Than or Equal To |
| `>=` | Greater Than or Equal To |
| `==` | Equal To |
| `!=` | Not Equal To |


## Logical Operators

| Symbol | Operation |
|---|---|
| `and` | Evaluates if all provided statements are True |
| `or` | Evaluates if at least one of many statements is True |
| `not` | Flips the Bool Value |


## Strings

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