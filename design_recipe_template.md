# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature



```python
# EXAMPLE

def check_for_todo(note):
    """Searches string for "#TODO"

    Parameters: (list all parameters and their types)
        note: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a boolean

    Side effects: (state any side effects)
        [Print error / raise exception] for invalid input
        i.e. list of integers, empty string

    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a string without the keyword
It returns False
"""
check_for_todo("Release the cat.") => False

"""
Given a string with the keyword
It returns True
"""
check_for_todo("Release the cat #TODO.") => True


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
