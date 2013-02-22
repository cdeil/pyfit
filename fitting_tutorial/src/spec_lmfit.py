from numpy import sqrt
from lmfit import Parameters, minimize
from spec import load_data, report_results

# Load data
x, y, y_err = load_data()

# Define model with named parameters
pars = Parameters()
pars.add('norm', value=1e-12)
pars.add('gamma', value=2)

def power_law(pars, x):
    norm = pars['norm'].value
    gamma = pars['gamma'].value
    return norm * x ** -gamma

# Define chi vector
# Nothe that (chi ** 2).sum() is automatically
# computed by minimize.
def chi(pars, x, y, y_err):
    model = power_law(pars, x)
    return (model - y) / y_err

# Perform fit
result = minimize(chi, pars, args=(x, y, y_err),
                  xtol=1e-15)

# Undo the s_factor, which was automatically applied by curve_fit
s_factor = (result.chisqr / result.nfree)

# Report results
# Can be either accessed by pars or equivalently by result.params
package = 'lmfit'
norm, gamma = pars['norm'].value, pars['gamma'].value
norm_err = pars['norm'].stderr / sqrt(s_factor)
gamma_err = pars['gamma'].stderr / sqrt(s_factor)
chi2 = result.chisqr
corr = pars['norm'].correl['gamma']
cov = corr * norm_err * gamma_err
report_results(package, norm, norm_err, gamma, gamma_err,
               chi2, cov, corr)

