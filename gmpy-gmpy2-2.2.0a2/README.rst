gmpy2 is an optimized, C-coded Python extension module that supports fast
multiple-precision arithmetic.  gmpy2 is based on the original gmpy module.
gmpy2 adds support for correctly rounded multiple-precision real arithmetic
(using the MPFR library) and complex arithmetic (using the MPC library).

Version 2.1.x Status
--------------------

gmpy2 2.1 was extensively refactored. Some of the significant changes are:

* Support for thread-safe contexts and context methods
* Interoperability with Cython extensions
* mpz and mpq operation can release the GIL

  * The current implementation is experimental

* Improved argument processing

The gmpy2 2.1 series will be the last to offer compatibility with Python 2.7.
Release 2.1.3 is the last planned release of the 2.1 series.

Note: Versions 2.1.4 and 2.1.5 were released to address Apple Silicon wheel
build issues. There are no code changes.

Release 2.1.5 is the last planned release of the 2.1 series.


Version 2.2 Plans
-----------------

Version 2.2 will drop support for Python 2.7 and older Python 3.x versions.

The primary development focus will be on functions that operate on lists and
release the GIL. See powmod_base_list and powmod_exp_list as examples.

Availability
------------

gmpy2 is available at https://pypi.python.org/pypi/gmpy2/

Documentation is available at https://gmpy2.readthedocs.io/en/latest/
