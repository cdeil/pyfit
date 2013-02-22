import os.path
dir = os.path.dirname(__file__)

def load_data():
    from numpy import loadtxt
    filename = os.path.join(dir, '../input', 'HESS_J1745-290.txt')
    data = loadtxt(filename)
    x, y = data[:, 0], data[:, 1]
    y_err = 0.5 * (data[:, 2] + data[:, 3])
    return x, y, y_err

def report_results(package, norm, norm_err, gamma, gamma_err,
                   chi2=None, cov=None, corr=None):
    filename = os.path.join(dir, '../output/spec', 
                            package + '.txt')
    print('Writing %s' % filename)
    f = open(filename, 'w')
    f.write('package: %s\n' % package)
    f.write('norm:  %g +- %g\n' % (norm, norm_err))
    f.write('gamma: %g +- %g\n' % (gamma, gamma_err))
    f.write('chi2: %s\n' % chi2)
    f.write('cov: %s\n' % cov)
    f.write('corr: %s\n' % corr)
    f.close()
    
if __name__ == '__main__':
    for script in ['scipy_curve_fit', 'lmfit', 'minuit']:
        filename = os.path.join(dir, 'spec_' + script + '.py')
        print('Running %s' % filename)
        execfile(filename)


