Packages
========

Below we give basic information and links for the Python modelling and fitting packages used in this tutorial.

In addition the ``numpy`` and ``pandas`` packages are used in almost every example, because they provide the basic data structures and file input / output capabilities:

* `Numpy <http://numpy.scipy.org>`_ has the `ndarray` for array data (e.g. histograms, images, time series, ...) and `recarray` for tabular data (e.g. parameters for observed events or objects). To learn about numpy, go to the `scipy-lectures tutorial <http://scipy-lectures.github.com/intro/numpy/index.html>`_, the `tentative NumPy tutorial <http://www.scipy.org/Tentative_NumPy_Tutorial>`_ and use the `numpy reference <http://docs.scipy.org/doc/>`_. The advantage of using numpy arrays to store data over using standard Python data types like lists and dicts is that numpy arrays use much less memory (depends, but a factor of 5 is typical) and processing them is much faster (depends on how it's done, but a factor 10 to 100 is typical).

* `Pandas <http://pandas.pydata.org>`_ has the ``Series``, ``DataFrame`` and ``Panel`` data structures for 1D, 2D and 3-dimensional data. Pandas has `great documentation <http://pandas.pydata.org/pandas-docs/stable/dsintro.html>`_. Pandas uses numpy arrays to implement it's data structure, so it's fast as well. You can think of the ``DataFrame`` as a numpy array on steroids.

And we use IPython and Cython:

* `IPython <http://ipython.org>`_  We use the IPython notebook as our data analysis environment, i.e. the place where we explore our data, implement our models and fit statistics, and finally perform our fits.

* `Cython <http://cython.org>`_ TODO: The dist_fit examples already use Cython. We should probably make an introductory page on when / how to use Cython to code the model or fit statistic and the speed-ups this gives.


`Scipy <scipy.github.com>`_
---------------------------

Scipy is probably the most-used scientific python package. It contains sub-packages on many different topics. For modelling and fitting mainly the `scipy.optimize` scipy_optimize_tutorial_ asdf


.. _scipy_optimize_reference: http://docs.scipy.org/doc/scipy/reference/optimize.html
.. _scipy_optimize_tutorial: http://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html
.. _scipy_stats_tutorial: http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
.. _scipy_other_tutorials: http://docs.scipy.org/doc/scipy/reference/tutorial/

.. _scipy_cookbooks: http://www.scipy.org/Cookbook
.. _scipy_cookbook_fitting_data: http://www.scipy.org/Cookbook/FittingData
.. _scipy_cookbook_linear_regression: http://www.scipy.org/Cookbook/LinearRegression
.. _scipy_cookbook_ols: http://www.scipy.org/Cookbook/OLS
.. _scipy_cookbook_circle: http://www.scipy.org/Cookbook/Least_Squares_Circle
.. _scipy_cookbook_ransac: http://www.scipy.org/Cookbook/RANSAC

TODO: use lmfit or statsmodels or scikit-learn for modelling / fitting instead of scipy directly.

`lmfit <http://newville.github.com/lmfit-py/>`_
-----------------------------------------------

``lmfit`` is a nice wrapper for the `scipy.optimize.leastsq <http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html>`_ as well as some of the other scipy optimizers and makes them available via the `lmfit.minimize <http://newville.github.com/lmfit-py/fitting.html#the-minimize-function>`_  and `lmfit.Minimizer <http://newville.github.com/lmfit-py/fitting.html#using-the-minimizer-class>`_ class. ``lmfit`` also provides the `lmfit.Parameter <http://newville.github.com/lmfit-py/parameters.html#the-parameter-class>`_ and `lmfit.Parameters <http://newville.github.com/lmfit-py/parameters.html#the-parameters-class>`_ classes that simplify modelling and fitting by giving each parameter a name and the possibility to set parameter bounds or to fix parameters. ``lmfit`` also has some methods to compute fit errors and confidence intervals. 

In addition 

* `uncertainties <http://packages.python.org/uncertainties/>`_ is a nice little package for 



* http://cxc.harvard.edu/contrib/sherpa/
* http://pymc-devs.github.com/pymc/
* http://statsmodels.sourceforge.net
* http://scikit-learn.org
* http://en.wikipedia.org/wiki/OpenOpt
* http://bethgelab.org/media/uploads/software/natter/doc/index.html
* http://sympy.org

* http://root.cern.ch/drupal/content/how-use-use-python-pyroot-interpreter
* http://code.google.com/p/pyminuit/
* http://code.google.com/p/pyminuit2/
* http://root.cern.ch/drupal/content/roofit
* https://github.com/piti118/RTMinuit
* https://github.com/piti118/dist_fit

There's more Python optimization packages listed in the
`topical software list at scipy.org <http://www.scipy.org/Topical_Software#head-d21a11d2d173826993e03eb937fac7e6347e6d5f>`_.



.. todo:: Add list of packages we have briefly looked at but don't want to investigate further?



http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html