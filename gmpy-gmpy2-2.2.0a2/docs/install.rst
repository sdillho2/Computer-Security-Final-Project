Installation
============

gmpy2 requires CPython 3.7 or above.  Pre-compiled binary wheels are available
on PyPI.  You can install latest release with pip::

    pip install gmpy2

or some specific version with::

    pip install gmpy2==2.1.5

If pre-compiled binary wheels aren't available for your platform, the pip will
fallback to installation from sources.  In this case you will need to have
required libraries (GMP, MPFR and MPC) already installed on your system, along
with the include files for those libraries.   On Debian you can install them
systed-wide with::

    sudo apt install libgmp-dev libmpfr-dev libmpc-dev

.. tip::

    On Windows we recommend using `MSYS2 <https://www.msys2.org/>`_ to build
    the gmpy2 from sources.  To install required dependencies before, run::

        pacman -S gcc gmp-devel mpfr-devel mpc-devel python-setuptools python-pip

From Sources
------------

If you are a developer or like to get the latest updates as they come, be sure
to install from the git repository and include required extra dependencies,
for example the optional "tests" list, which include packages required
for testing::

    git clone git://github.com/aleaxit/gmpy.git
    cd gmpy
    pip install -e .[tests]

Next you may want to run full set of unit tests to make sure everything works::

    pytest test/
