"""This is the example from the curve_fit docstring"""
import numpy as np
from scipy.optimize import curve_fit, fmin
def func(x, a, b, c):
    return a * np.exp(-b * x) + c
p0 = (2.5, 1.3, 0.5)
x = np.linspace(0, 4, 50)
y = func(x, *p0)
np.random.seed(0)
yn = y + 0.2 * np.random.normal(size=len(x))
popt, pcov = curve_fit(func, x, yn)
print 'curve_fit results:'
print 'values:', popt
print 'errors:', np.sqrt(pcov.diagonal())

"""And here is how to compute the fit parameter values and errors
using one of the other optimizers (exemplified with fmin) and 
a method to compute the Hesse matrix"""
def chi2(pars):
    chi = yn - func(x, *pars)
    return (chi ** 2).sum()
popt = fmin(chi2, p0, disp=False)
from numpy.dual import inv
from scikits.statsmodels.sandbox.regression.numdiff import approx_hess3 as approx_hess
phess = approx_hess(popt, chi2)
def approx_covar(hess, red_chi2):
    return red_chi2 * inv(phess / 2.)
red_chi2 = chi2(popt) / (len(x) - len(p0))
pcov = approx_covar(popt, red_chi2)
print 'fmin and approx_hess results:'
print 'values:', popt
print 'errors:', np.sqrt(pcov.diagonal())

"""Just to check, here is what Minuit has to say"""
from minuit import Minuit
def chi2(a, b, c):
    chi = yn - func(x, a, b, c)
    return (chi ** 2).sum()

m = Minuit(chi2, a=2.5, b=1.3, c=0.5)
m.migrad()
m.hesse()
pcov = red_chi2 * np.array(m.matrix())
popt = np.array(m.args)
print 'minuit results'
print 'values:', popt
print 'errors:', np.sqrt(pcov.diagonal())

try:
    raise
    import matplotlib.pyplot as plt
    plt.plot(x, yn, label='data')
    yfit = func(x, *popt)
    plt.plot(x, yfit, label='fit')
    plt.show()
except:
    print('No matplotlib, no plot')

