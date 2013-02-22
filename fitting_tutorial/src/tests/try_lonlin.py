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

"""Now do the same thing with statsmodels"""
from scikits.statsmodels.base.model import GenericLikelihoodModel
class NonLinearMLEModel(GenericLikelihoodModel):
    '''Maximum Likelihood Estimation of Linear Model with t-distributed errors

    This is an example for generic MLE.

    Except for defining the negative log-likelihood method, all
    methods and results are generic. Gradients and Hessian
    and all resulting statistics are based on numerical
    differentiation.'''

    def _predict(self, params, x):
        a, b, c = params
        return a * np.exp(-b * x) + c

    def geterrors(self, params):
        return self.endog - self._predict(params, x)

    def loglike(self, params):
        return -self.nloglikeobs(params).sum(0)

    def nloglikeobs(self, params):
        """
        Loglikelihood of non-linear model with normal distributed errors.

        Parameters
        ----------
        params : array
            The parameters of the model. The last parameters is scale.

        Returns
        -------
        loglike : array, (nobs,)
            The log likelihood of the model evaluated at `params` for each
            observation defined by self.endog and self.exog.

        Notes
        -----
        bla

        """
        from scipy import stats
        err = self.geterrors(params[:-1])
        return -stats.norm.logpdf(err, scale=np.abs(params[-1]))


class MyNonLinearMLEModel(NonLinearMLEModel):
    '''Maximum Likelihood Estimation of Linear Model with nonlinear function

    This is an example for generic MLE.

    Except for defining the negative log-likelihood method, all
    methods and results are generic. Gradients and Hessian
    and all resulting statistics are based on numerical
    differentiation.

    '''

    def _predict(self, params, x):
        a, b, c = params
        return a * np.exp(-b * x) + c


mod = MyNonLinearMLEModel(yn, x)
res = mod.fit(start_params=[1., 1., 1., 1.], disp=False)
# Note that the standard deviation in y is also
# estimated as a fourth parameter.
# We remove it here to compare to scipy
print 'values:', res.params[:-1]
print 'bse:   ', res.bse[:-1]
print 'bsejac:', res.bsejac[:-1]
print 'bsejhj:', res.bsejhj[:-1]    
