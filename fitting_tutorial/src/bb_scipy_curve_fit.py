import numpy as np
from numpy import sqrt
from scipy.optimize import curve_fit, leastsq
from bb import BoxBOD, report_results

# Perform fit
popt, pcov = curve_fit(BoxBOD.model, BoxBOD.x, BoxBOD.y, BoxBOD.p0)

def chi(pars):
    return BoxBOD.y - BoxBOD.model(BoxBOD.x, *pars)

res = leastsq(chi, BoxBOD.p0, full_output=True)
from pprint import pprint
pprint(res)
raise

# Report results
perr = sqrt(pcov.diagonal())
# chi2 is not returned, we have to compute it by hand
chi = (BoxBOD.y - BoxBOD.model(BoxBOD.x, *popt))
chi2 = (chi ** 2).sum()
report_results('scipy_curve_fit', popt, perr, chi2)

