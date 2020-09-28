# Python Docstring

- [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)


## Function Docstring

```py
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days.

    Args:
        days (int): number of days to convert

    Returns:
    string of the number of weeks and days included in days
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)
```