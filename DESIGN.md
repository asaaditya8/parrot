============
DESIGN
============

The library uses Command Pattern to compose a chain of rules from several rule instances.



Example Usage
~~~~~~~~~~~~~

    >>> class MyRule(RuleBase):
    >>>     def apply(self, x):
    >>>         # write your function here

    >>> data_obj = DataObj(data_str)
    >>>
    >>> rule1 = MyRule()
    >>> rule2 = AnotherRule()
    >>> chain = Sequential([
    >>>                       rule1,
    >>>                       rule2
    >>>                    ])
    >>>
    >>> result = chain(data_obj)