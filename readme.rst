==========================
IPython sphinx doc hosting
==========================

This repo is used to host builds of the IPython sphinx docs. The actual code
is in a `separate repo <http://github.com/ipython/ipython>`_.

How to build sphinx docs
------------------------

To make a new build, simply go to the doc directory and type::

    $ make gh-pages

or equivalently::

    $ make html
    $ ./gh-pages.py

This will create a new build of the docs tagged by 'git describe'. To
make something tagged with 'current', simply do::

    $ make gh-pages-current

or equivalently::

    $ ./gh-pages.py current

It may be a good idea to simply use 'current' for any builds of current
development that haven't been tagged.


.. [datarray] This readme, the index.html, and the scripts to update it, are adapted from `fperez/datarray <https://github.com/fperez/datarray-doc>`_