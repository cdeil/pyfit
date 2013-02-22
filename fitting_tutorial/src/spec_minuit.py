from minuit import Minuit
from spec import load_data, report_results

# Load data
x, y, y_err = load_data()

# Define model
def power_law(x, norm, gamma):
    return norm * x ** -gamma

# Define fit statistic
def chi2(norm, gamma):
    model = power_law(x, norm, gamma)
    chi = (y - model) / y_err
    return (chi ** 2).sum()

# Perform fit
m = Minuit(chi2, norm=1e-12, gamma=2)
m.migrad()
m.hesse()
#m.minos()
#print 'matrix:\n', m.matrix()
#print 'errors: ', m.errors
#print 'merrors:', m.merrors

# Report results
package = 'minuit'
gamma, norm = m.values.values()
gamma_err, norm_err = m.errors.values()
chi2 = m.fval
cov = m.covariance[('norm', 'gamma')]
corr = m.matrix(correlation=True)[0][1]
report_results(package, norm, norm_err, gamma, gamma_err,
               chi2, cov, corr)

