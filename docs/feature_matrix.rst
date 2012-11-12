Feature Matrix
==============

The following feature matrix shows which package (rows) supports which feature (columns).
This will help you decide which package to use for your task.
If you're the package author, feel free to improve your package and let us know. :-)

The entries have the following meaning:

====== =======
Symbol Meaning
====== =======
`-`    not possible with this package
`0`    possible, but not explicitly supported, i.e. hard to do
`+`    supported
`++`   super-easy
`?`    we haven't looked at this yet; to be done ...
====== =======

.. note::
	We realize that the evaluations of different packages on this page is highly subjective.

	Please open an issue or pull request on github if you find something actually wrong
	(e.g. package X now has feature Y or our example code can be simplified or any other improvements).

.. todo:: How to make the text for the problems vertical?

=========  ======= ============= ========= ===== ============ ========================
Package    Install Documentation Modelling Speed Error Matrix Likelihood Profile Error
=========  ======= ============= ========= ===== ============ ========================
scipy      ++      ++            ++        ++           ++
sherpa     ++      ++            ++        ++           ++
RTMinuit   ++      ++            ++        ++           ++
=========  ======= ============= ========= ===== ============ ========================


.. todo:: other features to include in the table:

	* ability to check convergence
	* ability to get error matrix and making sure it's accurate
	* ability to get likelihood profile
	* ability to see if any variable hit the limit
	* ability to see if any thing went wrong in general: eg. it gives me an answer but... can I trust it

