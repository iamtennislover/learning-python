# Q7. make_dict. 2 pts

# Complete this function according to specificatin

def make_dict(keys, values):
    """Produces and returns a dictionary of keys to values. Items from iterables
    keys and values are consumed and paired in order as key-value pairs in the
    dictionary.

    If keys and values are not the same length, extraneous items of the longer
    list will be discarded.

    Examples:
    >>> make_dict([1,2,3],[4,5,6])
    {1:4, 2:5, 3:6}
    >>> make_dict(['one', 'two', 'three'], [1,2,3])
    {'one':1, 'two':2, 'three':3}
    >>> make_dict([1,2,3,4],[4,5,6])
    {1:4, 2:5, 3:6}
    >>> make_dict([1,2,3],[4,5,6,7])
    {1:4, 2:5, 3:6}
    """
    pass

k = [1,2,3,4]
v = [4,5,6,9]
do_the_dict = make_dict(k, v)
print("this is the dictionary with keys and values from the two lists", do_the_dict)