==================
Disable Docstrings
==================

This is a Nose_ plugin that tells unittest not to use test docstrings as
test names. Instead it uses the name of the test itself.

Install::

  git clone git@github.com:gabend/disable-docstring.git
  cd disable-docstring
  python setup.py install

Usage::

This plugin is on by default, replacing the docstrings in test output.
To disable the effects of this plugin, add the following commandline option:

  nosetests -v --enable-docstring

.. _Nose: http://somethingaboutorange.com/mrl/projects/nose/
