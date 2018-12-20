from collections import Iterable

isinstance('abcd', Iterable)  # str是否可迭代
# isinstance('[1,2,3,4]', Iterable)   list是否可迭代
# isinstance(123, Iterable)   整数是否可迭代
