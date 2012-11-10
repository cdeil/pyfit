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
def g(x,mu,resolution):
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

# <codecell>


# <codecell>


# <codecell>


# <codecell>


