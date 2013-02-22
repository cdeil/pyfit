"""
scipy.optimize.curve_fit has a weird covariance matrix scaling
factor applied at the end:

https://github.com/scipy/scipy/blob/master/scipy/optimize/minpack.py#L438
    s_sq = (func(popt, *args)**2).sum()/(len(ydata)-len(p0))
    pcov = pcov * s_sq

Note that func is 
    chi = w * (f - y),
so covariances are actually scaled by 
    s_sq = sum(chi ** 2) / dof.
This factor also appears in http://en.wikipedia.org/wiki/Regression_analysis,
where it is written as
    sigma_epsilon_sq = SSE / N - 2, 
    with SSE = sum(chi ** 2),
    N the number of data points
    and 2 the number of parameters,
    i.e. dof = N - 2.

The same pcov could have been obtained if the chi function had been
modified to
??? chi2 = (y-f)**2
because
???
"""
import numpy as np

if True:
    """Example from http://code.google.com/p/pyminuit/wiki/GettingStartedGuide"""
    x = np.array([1  , 2  , 3  , 4  ])
    y = np.array([1.1, 2.1, 2.4, 4.3])
    sigma = np.array([0.1, 0.1, 0.2, 0.1])
else:
    """Example from http://mail.scipy.org/pipermail/scipy-user/2011-August/030412.html"""
    x = np.arange(5)
    y = np.array([1, -2, 1, -2, 1])
    sigma = 10 * np.array([1, 2, 1, 2, 1])

def f(x, a, b):
    return a + b * x

def chi(a, b):
    return (f(x, a, b) - y) / sigma

def chi2(a, b):
    return (chi(a, b) ** 2).sum()

def run_WLS():
    import scikits.statsmodels.api as sm
    res = sm.WLS(y, sm.add_constant(x, prepend=True),
                 weights=1. / sigma ** 2).fit()
    print ('statsmodels.api.WLS')
    print('popt: {0}'.format(res.params))
    print('perr: {0}'.format(res.bse))
    return res

def run_NonlinearLS():
   from scikits.statsmodels.miscmodels.nonlinls import NonlinearLS
   class Myfunc(NonlinearLS):
       def _predict(self, params):
           x = self.exog
           a, b = params
           return a + b * x
   mod = Myfunc(y, x, sigma=sigma ** 2)
   res = mod.fit(start_value=(0.042, 0.42))
   print ('statsmodels NonlinearLS')
   print('popt: {0}'.format(res.params))
   print('perr: {0}'.format(res.bse))

def run_curve_fit():
    from scipy.optimize import curve_fit
    res = curve_fit(f, x, y, p0=(5, 10.1), sigma=sigma,
                    ftol=1e-15, full_output=True)
    (popt, pcov, infodict, errmsg, ier) = res
    #print errmsg
    #print ier
    perr = np.sqrt(pcov.diagonal())
    print ('scipy.optimize.curve_fit')
    print('popt: {0}'.format(popt))
    print('perr: {0}'.format(perr))

def run_minuit():
    from minuit import Minuit
    m = Minuit(chi2, b=5, a=10)
    m.migrad()
    m.hesse()
    popt = m.values.values()
    perr = np.array(m.errors.values())
    # In scipy.optimize.curve_fit, the following factor is applied
    #            cov = cov * sum_sqr / self.nfree
    factor = m.fval / (len(x) - 2)
    perr *= np.sqrt(factor)
    print ('minuit')
    print('popt: {0}'.format(popt))
    print('perr: {0}'.format(perr))

if __name__ == '__main__':
    for run in [run_WLS, run_NonlinearLS,
                run_curve_fit, run_minuit]:
        try:
            run()
        except ImportError:
            print('%s not available.' % run)
