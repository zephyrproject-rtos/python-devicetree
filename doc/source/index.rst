python-devicetree
=================

This is part of an ongoing effort to extract the Zephyr Project's
`devicetree tools`_ to a standalone location for wider use.

This is version |release|. It is based on the Zephyr tools as of commit
`f5409dec01`_.

.. _devicetree tools:
   https://docs.zephyrproject.org/latest/guides/dts/intro.html#scripts-and-tools

.. _f5409dec01:
   https://github.com/zephyrproject-rtos/zephyr/commit/f5409dec01c84aa8eda1830c64309abe3d5868d0

Quickstart
==========

.. code-block:: sh

   $ pip3 install devicetree
   $ python3
   [...]
   >>> from devicetree import edtlib, dtlib

Then you should be able to use :ref:`edtlib` and :ref:`dtlib` in the same way
Zephyr does with its in-tree versions of these modules.

This is meant as a way to get started. Breaking API changes to make this code
easier to use standalone are possible.

.. toctree::
   :maxdepth: 2
   :hidden:

   dtlib
   edtlib
