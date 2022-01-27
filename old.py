
# Q1. calculate_total. 2 points

# Debug the following function so that it will successfully return the sum of
# the of the numbers passed as args. Note: there is more than one error here!

# IMPORTANT: See the example of how calculate_total should be called! Do not
# pass a list into calculate total!

# HINT: The fix will require a change to the function's API signature. This is
# one of only 2 problems in the exam that require a change to the function
# signature!!!

def calculate_total(*numbers):
    """Return the sum of the numbers.

    Example:
    >>> calculate_total(1,2,3)
    6
    """
    t_ = 0
    for i in numbers:
      t_ += i
    return t_

# As you complete your test, you will typically want to add calls like this to
# see that you are getting expected results. It is fine to add these calls and
# other code below the function defintion -- just don't define new functions
# with names that are the same as other functions in the test

print(calculate_total(1,2,3)) # Do not pass a list object to calculate_total!



# Q6. concat_all. 1 point

# Complete function concat_all according to the specification. The function
# should return the string of all items in the list concatenated.

def concat_all(list_of_strings):
  """Return the string concatenation of all strings in the list.

    Example:
    >>> concat_all(['red', 'orange', 'yellow'])
    'redorangeyellow'
    >>> concat_all(['green', 'blue', 'violet'])
    'greenblueviolet'
  """
  r = ""
  for s in list_of_strings:
    r = r + s
  return r

print("concat_all1", concat_all(['red', 'orange', 'yellow']))
print("concat_all1", concat_all(['green', 'blue', 'violet']))



# Q9. loglines. 1 point

# Sometimes logging is too verbose. The following function takes a parameter n
# (which defaults to 10) with the intention of printing only the first line
# and every nth line after it. However, as-is the code simply prints all the lines.

# Fix the code to utilize the customizable parameter n.

def loglines(lines, n=10):
    """Print the first and every nth line of lines.
    
    E.g. loglines of the letters of the alphabet, with n=2 will print:

    a
    c
    e
    g
    ... etc.
    """
    for i, l in enumerate(lines):
        if i % n == 0:
          print(l)

loglines(["a", "b", "c", "d", "e", "f", "g"], n=2)



# Q13. inject. 2 points

# The code below throws an AttributeError. Debug and fix this function to work
# according to specification.

def inject(s, i):
    """Return a string like s, but with i injected as every other letter
    within the string. Only inject i within the string, not before the first
    letter of s or after the last letter of s.

    The code should handle both strings and numeric values, returning a string
    in either case.

    Examples:
    >>> inject('Hello world', 'x')
    'Hxexlxlxox xwxoxrxlxd'
    >>> inject(7334, 3)
    '7333334'
    """
    n = ""
    for c in str(s):
      n = n + c + str(i)
    return n[:-1]

print("inject1", inject('Hello world', 'x'))
print("inject2", inject(7334, 3))

# amul: donedonandoneonde

# Q15. nth_item. 2 points

# Complete the function nth_item according to the specification.

# Q30. compare. 2 points

# Debug this code so that it results in a simple comparison function that
# returns the natural language comparison of two values.

def compare(a, b):
    """Return the natural language comparison of a to b. Return values are:
        'same as'
        'greater than'
        'less than'

    Invalid comparisons should return 'unknown'

    Examples
    >>> compare(1, 2)
    'less than'
    >>> compare('a', 1)
    'unknown'
    """
    if type(a) != type(b):
      return 'unknown'

    if a == b:
        return 'same as'
    elif a > b:
        return 'greater than'
    elif a < b:
        return 'less than'

print(compare(1, 2))
print(compare('a', 1))



# Q29. is_zero. 1 point

# Some of our data needs to be cleaned, and we want to consider cases of None
# to be considered the value 0. Anything else that is not actually a numeric 0
# should not be considered 0. This means the empty string '', the string 'zero',
# and the string '0' should all return false. 

def is_zero(val):
    """Return True if val is 0 or None. Otherwise return False.

    Examples:
    >>> is_zero(0)
    True
    >>> is_zero(None)
    True
    >>> is_zero('')
    False
    """
    if val == 0:
      return True
    if val == None:
      return True
    return False
    
print(is_zero(0))
print(is_zero(None))
print(is_zero(""))




# Q10. multiply. 2 points

# Python's * operator is overloaded for numbers and strings. It multiplies
# numbers mathematically, but "multiplies" strings by repeating the string n
# times. E.g. 'foo'*3 == 'foofoofoo'

# Create a function called multiply that treats all inputs the way Python
# multiplies strings. E.g. multiply(1, 3) == '111', not 3

def multiply(val, n):
    """Return val * n operated as if val were a string even if it is a number.

    Examples:
    >>> multiply('one', 3)
    'oneoneone'
    >>> multiply(1, 3)
    '111'
    """
    return str(val)*n

print(multiply('one', 3))
print(multiply(1, 3))


# Q16. nth_last_item. 2 points

# Complete the function nth_last_item according to the specification.

def nth_last_item(item_list, n):
    """Return the item of item_list that is the nth value from the last in the
    List. Thus, when n is 1, return the last item of the list.

    If n is zero or larger than the length of the list, or if n is negative,
    return None.

    Examples:
    >>> nth_last_item(['one', 'two', 'three'], 1)
    'three'
    >>> nth_last_item(['one', 'two', 'three'], 3)
    'one'
    >>> nth_last_item(['one', 'two', 'three'], 0)
    >>> nth_last_item(['one', 'two', 'three'], -1)
    """
    if n == 1:
      return item_list[-1]
    if n == 0 or n > len(item_list) or n <0:
      return None
    else:
      return item_list[-n]

print(nth_last_item(['one', 'two', 'three'], 1))
print(nth_last_item(['one', 'two', 'three'], 3))
print(nth_last_item(['one', 'two', 'three'], 0))
print(nth_last_item(['one', 'two', 'three'], -1))
