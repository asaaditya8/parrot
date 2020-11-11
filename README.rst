======
parrot
======


.. image:: https://travis-ci.org/asaaditya8/parrot.png?branch=master
    :target: https://travis-ci.org/asaaditya8/parrot

.. image:: https://badge.fury.io/py/parrot.png
    :target: http://badge.fury.io/py/parrot

.. image:: https://coveralls.io/repos/asaaditya8/parrot/badge.png?branch=master
    :target: https://coveralls.io/r/asaaditya8/parrot?branch=master

.. image:: https://pypip.in/d/parrot/badge.png
        :target: https://crate.io/packages/parrot?version=latest

``parrot`` - Thi is aimed at converting transcription of spoken english to written english.

Features
--------

* TODO

==============  ==========================================================
Python support  Python 2.7, >= 3.3
Source          https://github.com/asaaditya8/parrot
Docs            http://parrot.rtfd.org
Changelog       http://parrot.readthedocs.org/en/latest/history.html
API             http://parrot.readthedocs.org/en/latest/api.html
Issues          https://github.com/asaaditya8/parrot/issues
Travis          http://travis-ci.org/asaaditya8/parrot
Test coverage   https://coveralls.io/r/asaaditya8/parrot
pypi            https://pypi.python.org/pypi/parrot
Ohloh           https://www.ohloh.net/p/parrot
License         `BSD`_.
git repo        .. code-block:: bash

                    $ git clone https://github.com/asaaditya8/parrot.git
install dev     .. code-block:: bash

                    $ git clone https://github.com/asaaditya8/parrot.git parrot
                    $ cd ./parrot
                    $ virtualenv .env
                    $ source .env/bin/activate
                    $ pip install -e .
tests           .. code-block:: bash

                    $ python setup.py test
==============  ==========================================================

Example Usage
-------------

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

.. _BSD: http://opensource.org/licenses/BSD-3-Clause
.. _Documentation: http://parrot.readthedocs.org/en/latest/
.. _API: http://parrot.readthedocs.org/en/latest/api.html
