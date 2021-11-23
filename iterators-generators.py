"""
# Iterable/iterator
>>> l = [1, 2]
>>> i = iter(l)
>>> type(l)
<class 'list'>

>>> type(i)
<class 'list_iterator'>

>>> l.__next__()
Traceback (most recent call last):
...
AttributeError: 'list' object has no attribute '__next__'

>>> i.__next__()
1

>>> i.__next__()
2

>>> i.__next__()
Traceback (most recent call last):
...
StopIteration


>>> i.__iter__() #doctest: +ELLIPSIS
<list_iterator object ...>

# Range
>>> r = range(1)
>>> type(r)
<class 'range'>

>>> r.__iter__() #doctest: +ELLIPSIS
<range_iterator object ...>

>>> r.__next__()
Traceback (most recent call last):
...
AttributeError: 'range' object has no attribute '__next__'

# Enumerate
>>> type(enumerate([1]))
<class 'enumerate'>

>>> enumerate([1, 2, 3]) #doctest: +ELLIPSIS
<enumerate object ...>

>>> enumerate((1, 2, 3)) #doctest: +ELLIPSIS
<enumerate object ...>

>>> enumerate({1, 2, 3}) #doctest: +ELLIPSIS
<enumerate object ...>

>>> enumerate({ "a": 1 }) #doctest: +ELLIPSIS
<enumerate object ...>

>>> enumerate("string") #doctest: +ELLIPSIS
<enumerate object ...>

>>> tuple(enumerate(['a', 'b', 'c']))
((0, 'a'), (1, 'b'), (2, 'c'))

>>> for i, element in enumerate("abc"):
...     print(i, element)
0 a
1 b
2 c
"""

def iterable(obj):
    """
    # Iterable example
    >>> iterable([1, 2, 3]) 
    True

    >>> iterable((1, 2, 3))
    True

    >>> iterable({1, 2, 3})
    True

    >>> iterable({ "a": 1 })
    True

    >>> iterable(1)
    False

    >>> iterable("string")
    True
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False

def range_custom(start, end):
    """
    # Generator
    >>> g = range_custom(1, 3)
    >>> type(g)
    <class 'generator'>

    >>> g #doctest: +ELLIPSIS
    <generator object ...>

    >>> iter(g) #doctest: +ELLIPSIS
    <generator object ...>

    >>> next(g)
    1

    >>> next(g)
    2

    >>> next(g)
    Traceback (most recent call last):
    ...
    StopIteration
    """
    while start < end:
        yield start
        start += 1
