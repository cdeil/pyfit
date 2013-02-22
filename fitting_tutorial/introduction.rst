Introduction
============

Fitting involves the following five components:

* Data
* Model (contains a list of parameters)
* Statistic
* Optimizer
* Results

The statistic combines the data and model, you can think of it as
a function ``statistic(parameters)`` of the  model parameters.

It is the optimizers job to compute the minimum of of the statistic
function as well as characterize the errors on the best-fit parameters.

Note that not all five components exist as objects or functions in every package:

* Sometimes the results are stored in the model or optimizer object,
  sometimes it is a separate object returned by a call
  ``results = optimizer(statistic)``

* Sometimes the statistic is constructed implicitly by the optimizer,
  i.e. the API is:
  ``results = optimizer(model, data)``

These differences can be confusing when you start using a new package,
so before you look at the concrete examples, here is a summary table:

What does it mean to fit data?
++++++++++++++++++++++++++++++

TODO: Give definitions

* Describe ``chi2`` and ``nll`` function
* Best-fit parameters are the ones that minimize chi2
* Covariance matrix is defined as inverse of (TODO: factor 2?) the Hessian 
  (i.e. the matrix of second derivatives at the minimum)
* Parameter errors are defined as sqrt of covariance matrix
* Covariance matrix can also be computed from Jacobian how?
  see leastsq docstring and statistics textbooks.
* Define ``s_factor``

.. code-block:: python

   # Data
   x, y, sigma = ...
   
   # Model
   def power_law(x, norm, gamma):
       return norm * x ** -gamma
   
   # Fit statistic
   def chi2(norm, gamma):
       model = power_law(x, norm, gamma)
       chi = (y - model) / y_err
       return (chi ** 2).sum()

.. note::
   To reproduce these results an ``s_factor`` has to be applied
   to the errors. This is done automatically by ``scipy.optimize.curve_fit``
   and by ``lmfit.minimize``, but not by ``minuit`` or ``sherpa``.


TODO
++++

* Define chi2 and logL (or cash?) statistic here. 
* Make a summary table: package vs the five components above and
  mention for each if it is an object or a function or not
  visible at all to the user.
  