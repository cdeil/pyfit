from numpy import sqrt
from minuit import Minuit
from bb import BoxBOD, report_results

# Load data
x, y = BoxBOD.x, BoxBOD.y

# Define fit statistic
def chi2(b1, b2):
    model = BoxBOD.model(x, b1, b2)
    chi = y - model 
    return (chi ** 2).sum()

# Perform fit
m = Minuit(chi2, b1=BoxBOD.p0[0], b2=BoxBOD.p0[1])
m.migrad()
m.hesse()
print(m.matrix())

# Report results (we have to apply the s factor ourselves)
popt = m.values.values()
chi2 = m.fval
ndf = len(x) - len(m.values)
s_factor = sqrt(chi2 / ndf)
perr = s_factor * m.errors.values()
report_results('minuit', popt, perr, chi2)
