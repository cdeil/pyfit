Python fitting tutorial
=======================

Contents:

.. toctree::
   :maxdepth: 1

   introduction
   spec
   image
   bb
   
There are several python packages for fitting data with some parameterized model.
We showcase solutions to two common example fitting problems in a number of packages you might consider.
Browsing this tutorial will only take you 15 minutes and help you choose a package you like,
before you invest hours to install and learn a package only to find out you don't like it.

The examples:

* Chi2 fit of a 1D power-law model to spectral flux points (real HESS data)
* Poisson likelihood fit of a 2D symmetric Gaussian on flat background (simulated data)
* The BoxBOD example was only added because I got inconsistent results
  from ``scipy.optimize.curve_fit`` because I did not know about the ``s_factor``.
  

The optimizers:

* `scipy.optimize.fmin`_ -- calls Nelder-Mead simplex algorithm from TODO
* `scipy.optimize.leastsq`_ -- calls Levenberg-Marquard optimizer from MINPACK (lmdif and lmder)
* `scipy.optimize.curve_fit`_ -- A simplified wrapper around `scipy.optimize.leastsq`_
* `lmfit`_ -- nice interface (parameter names, fix/free, min/max) around `scipy.optimize.leastsq`_
* `statsmodels`_ --
* `pymc`_ -- Mostly for `MCMC`_ fitting, but also includes a 
  `NormApprox`_ class that wrap the conventional scipy optimizers.
* `pyminuit`_ -- Python interface to `MINUIT`_
* `sherpa`_ --
* TODO complete list (or better yet make this a table with more info)
* Others -- see this `list of python optimizers`_

Note that many more python fitting (a.k.a. optimization or minimization) packages exist.
Each has its own set of advantages and disadvantages, 
some of the criteria you might want to look for in a fitting
package while browsing the following tutorial are:

* User friendlyness -- Does it have a nice API to define models,
  and fit statistics and load your data?
  Is there good documentation and a helpful community? 
* Functionality -- Can I code my own models and fit statistics?
  Are there methods to compute the covariance matrix or asymmetric
  parameter limits?
* Fast -- Which optimizers are available?
* Installation -- Is the package easy and fast to install?
  Some packages pure Python and are installed in 10 seconds using one command
  ``pip install lmfit``, others (like Sherpa) can take you hours
  to figure out how to build on your system because they depend on many
  C and Fortran extensions.

.. _scipy.optimize.fmin: http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html#scipy.optimize.fmin
.. _scipy.optimize.leastsq: http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fmin.html#scipy.optimize.fmin
.. _scipy.optimize.curve_fit: _http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
.. _lmfit: http://newville.github.com/lmfit-py/
.. _statsmodels: http://statsmodels.sourceforge.net/devel/
.. _pymc: http://code.google.com/p/pymc/
.. _MCMC: http://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo
.. _NormApprox: http://pymc.googlecode.com/svn/doc/modelfitting.html#normal-approximations
.. _pyminuit: http://code.google.com/p/pyminuit/
.. _MINUIT: http://en.wikipedia.org/wiki/MINUIT
.. _sherpa: http://cxc.harvard.edu/sherpa
.. _sherpa tutorial: http://cxc.cfa.harvard.edu/contrib/sherpa/scipy11/
.. _openopt: http://openopt.org
.. _mystic: http://dev.danse.us/trac/mystic
.. _list of python optimizers: http://scipy.org/Topical_Software#head-d21a11d2d173826993e03eb937fac7e6347e6d5f

TODO
++++

.. todo:: Add scipy.optimize.fmin and statsmodels as example optimizers

.. todo::
   Investigate the xtol and ftol parameters of the different packages.
   What are actually the stopping conditions and how do the specified
   xtol or ftol correspond to actual xtol or ftol achieved?
 
 .. todolist::
 
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

