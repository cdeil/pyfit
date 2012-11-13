# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from dist_fit import *
%load_ext cythonmagic

# <headingcell level=2>

# Crystalball

# <codecell>

bound = (-100,100)
ncball = Normalize(crystalball, bound)
print describe(ncball)
np.random.seed(0)#make sure we get consistent result
cball_toy = gen_toy(ncball,10000, bound, alpha=1.,n=1.5,mean=20,sigma=10)
hist(cball_toy,bins=100,histtype='step');
np.savetxt('crystalball.csv',cball_toy)
print cball_toy[:5]

# <headingcell level=2>

# Gaussian Convoluted Crystalball

# <codecell>

%%cython
#this is stupid but there is a name clash from crystalball and gaussian
cimport cython
from libc.math cimport exp, M_PI
@cython.binding(True)
def g(double x,double mu,double resolution):
    return 1./2./M_PI*exp(-(x-mu)**2/2./resolution)

# <codecell>

gcball = Convolve(g,crystalball,bound)
ngcball = Normalize(gcball,bound)
print describe(gcball)
np.random.seed(0)
gcball_toy = gcball_toy = gen_toy(ngcball,10000,bound,
    mu=-20.,resolution=10.,alpha=1.,n=1.5,mean=20.,sigma=10.)

# <codecell>

hist(gcball_toy,bins=100,histtype='step');
np.savetxt('crystallball_convoluted.csv',gcball_toy)

# <headingcell level=2>

# Gaussian

# <codecell>

np.random.seed(0)
gauss_toy = randn(10000)*2+1.0
hist(gauss_toy,100,histtype='step');
np.savetxt('gaussian.csv',gauss_toy)

# <headingcell level=1>

# Gaussian with Linear Background

# <codecell>

%%cython
cimport cython
from dist_fit import Normalize
from libc.math cimport exp, M_PI
cdef inline double g(double x,double mu,double resolution):
    return 1./2./M_PI*exp(-(x-mu)**2/2./resolution)

@cython.binding(True)
def linear(double x,double m,double c):
    return m*x+c

nlin = Normalize(linear,(0,5))

@cython.binding(True)
def gauss_linear(double x,
    double m,double c,
    double mu,double sigma,double nsig,double nbg):
    cdef double gau = g(x,mu,sigma)
    cdef double lin = nlin(x,m,c) 
    return nsig*gau+nbg*lin

# <codecell>

ngauss_linear = Normalize(gauss_linear,(0,5))
np.random.seed(0)
gl_toy = gen_toy(ngauss_linear,10000,(0,5), m=2., c=0., mu=2.,sigma=0.1,nsig=100,nbg=30)

# <codecell>

hist(gl_toy,bins=100,histtype='step');
np.savetxt('gaussian_linear.csv',gl_toy)

# <codecell>


