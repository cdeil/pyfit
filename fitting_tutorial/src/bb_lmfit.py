from lmfit import Parameters, minimize
from bb import BoxBOD, report_results

# Define model with named parameters
pars = Parameters()
pars.add('b1', value=BoxBOD.p0[0])
pars.add('b2', value=BoxBOD.p0[1])

def model(pars, x):
    b1 = pars['b1'].value
    b2 = pars['b2'].value
    return BoxBOD.model(x, b1, b2)

# Define chi vector
# Nothe that (chi ** 2).sum() is automatically
# computed by minimize.
def chi(pars, x, y):
    return model(pars, x) - y

# Perform fit
result = minimize(chi, pars, args=(BoxBOD.x, BoxBOD.y))

# Report results
popt = [pars['b1'].value, pars['b2'].value]
perr = [pars['b1'].stderr, pars['b2'].stderr]
chi2 = result.chisqr
report_results('lmfit', popt, perr, chi2)

