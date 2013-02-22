import os.path
dir = os.path.dirname(__file__)
import numpy as np
from numpy import exp

class BoxBOD(object):
    '''This is the reference dataset and fit results from NIST,
    copy & pasted from the following file
    http://www.itl.nist.gov/div898/strd/nls/data/LINKS/DATA/BoxBOD.dat
    '''
    # Data and Model
    nobs = 6
    x = np.array([1, 2, 3, 5, 7, 10], dtype=float)
    y = np.array([109, 149, 149, 191, 213, 224], dtype=float)
    @staticmethod
    def model(x, b1, b2):
        return b1 * (1 - exp(-b2 * x))
    # Results
    pnames = ['b1', 'b2']
    pstart = np.array([1, 1], dtype=float)
    pstart2 = np.array([100, 0.75], dtype=float)
    # Fit convergence is hard, so we choose very close start values
    p0 = np.array([200, 0.5], dtype=float)
    popt = np.array([2.1380940889e+02, 5.4723748542e-01])
    perr = np.array([1.2354515176e+01, 1.0455993237e-01])
    dof = 4
    chi2 = 1.1680088766e+03
    resid_std = 1.7088072423e+01

def report_results(package, popt, perr, chi2):
    filename = os.path.join(dir, '../output/bb', 
                            package + '.txt')
    f = open(filename, 'w')
    print('Writing %s' % filename)
    f.write('package: %s\n' % package)
    f.write('popt: %s\n' % popt)
    f.write('perr: %s\n' % perr)
    f.write('chi2: %s\n' % chi2)
    popt_diff = (popt - BoxBOD.popt) / BoxBOD.popt
    perr_diff = (perr - BoxBOD.perr) / BoxBOD.perr
    chi2_diff = (chi2 - BoxBOD.chi2) / BoxBOD.chi2
    f.write('popt_diff: %s\n' % popt_diff)
    f.write('perr_diff: %s\n' % perr_diff)
    f.write('chi2_diff: %s\n' % chi2_diff)
    f.close()

if __name__ == '__main__':
    for script in ['scipy_curve_fit', 'lmfit', 'minuit']:
        filename = os.path.join(dir, 'bb_' + script + '.py')
        print('Running %s' % filename)
        execfile(filename)
