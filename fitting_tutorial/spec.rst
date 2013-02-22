Chi2-Fit using a power-law model and spectral flux points
=========================================================

Dataset
+++++++

HESS Galactic center published spectral points.

.. http://www.mpi-hd.mpg.de/hfm/HESS
.. http://aps.arxiv.org/abs/0906.1247
.. http://www.mpi-hd.mpg.de/hfm/HESS/pages/publications/auxiliary/GC_Spectrum_Points.html

Results
+++++++

.. note::
   The scipy_curve_fit and lm_fit results are very inaccurate.
   Fiddle with parameters to make this work and explain the problem in
   this tutorial as a showcase that you should never blindly trust
   fitting results and what diagnostics tools are available.

.. literalinclude:: output/spec/scipy_curve_fit.txt
.. literalinclude:: output/spec/lmfit.txt
.. literalinclude:: output/spec/minuit.txt
.. literalinclude:: output/spec/sherpa.txt

Plot
++++

.. todo:: Show a script how to e2dnde plot flux points and a butterfly of the model.
