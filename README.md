python_modelling_fitting
========================

What is this?
-------------

A survey / tutorial of existing Python modelling and fitting packages.

What is this (long version)?
----------------------------

Modelling and fitting data is a very common data analysis task for scientists and engineers.
This is often a trial-and-error activity, one has to try out different models, fit parameter
starting values and sometimes even fit statistics (a.k.a. cost functions like chi-square or
likelihood).
The Python programming language and the IPython shell are a very good and popular
choice for modelling and fitting, and indeed there are plenty of Python packages for modelling
and / or fitting available:

* http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
* http://newville.github.com/lmfit-py/
* http://cxc.harvard.edu/contrib/sherpa/
* http://pymc-devs.github.com/pymc/
* http://statsmodels.sourceforge.net
* http://scikit-learn.org
* http://en.wikipedia.org/wiki/OpenOpt
* http://bethgelab.org/media/uploads/software/natter/doc/index.html
* http://sympy.org

The most popular modelling and fitting package used by physicists is ROOT / Minuit / RooFit.
It's C++ though, and the existing CINT command line interface is not as nice as IPython.
There have been several projects wrapping ROOT / Minuit / RooFit in Python:

* http://root.cern.ch/drupal/content/how-use-use-python-pyroot-interpreter
* http://code.google.com/p/pyminuit/
* http://code.google.com/p/pyminuit2/
* http://root.cern.ch/drupal/content/roofit
* https://github.com/piti118/RTMinuit
* https://github.com/piti118/dist_fit

Here we want to survey the existing Python packages to see what their features and user interface are,
before we attempt to add Minuit and / or RooFit Python wrappers to rootpy ( http://www.rootpy.org ).

We'll take a few simple to medium-difficulty fitting problems and show how to solve them with each package.
This should also be a nice tutorial for people that are trying to decide which package is worth learning
and will be the best for their analysis needs.

All help is welcome!

