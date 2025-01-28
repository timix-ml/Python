"""
Методика тестирования, посредством написания доктестов

py -m doctest -v test-doc.py
py test-doc.py -v
"""


def ml(i: int) -> int:
    """
    >>> ml(2)
    4

    >>> ml(10)
    100

    >>> ml("str")
    Traceback (most recent call last):
        ...
    TypeError: can't multiply sequence by non-int of type 'str'
    """
    return i * i


def lml(i: int) -> list[int]:
    """
    >>> lml(2)
    [2, 2]

    >>> lml(10) # doctest: +ELLIPSIS
    [10, ..., 10]

    >>> lml("str")
    Traceback (most recent call last):
        ...
    TypeError: can't multiply sequence by non-int of type 'str'
    """
    return [i] * i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
