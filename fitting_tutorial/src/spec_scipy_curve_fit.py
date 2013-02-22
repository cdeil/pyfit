from numpy import sqrt
from scipy.optimize import curve_fit
from spec import load_data, report_results

# Define model
def power_law(x, norm, gamma):
    return norm * x ** -gamma

# Load data
x, y, y_err = load_data()

# Perform fit
popt, pcov = curve_fit(power_law, x, y,
                       p0=(1e-12, 2), sigma=y_err,
                       xtol=1e-15)

# chi2 is not returned, we have to compute it by hand
chi = (y - power_law(x, *popt)) / y_err
chi2 = (chi ** 2).sum()

# Undo the s_factor, which was automatically applied by curve_fit
dof = len(x) - len(popt)
s_factor = (chi2 / dof)
pcov /= s_factor

# Report results
package = 'scipy_curve_fit'
norm, gamma = popt
norm_err, gamma_err = sqrt(pcov.diagonal())
cov = pcov[0, 1]
corr = cov / (norm_err * gamma_err)
report_results(package, norm, norm_err, gamma, gamma_err,
               chi2, cov, corr)

