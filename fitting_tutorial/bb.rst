Chi2-Fit for BoxBOD
===================

`BoxBOD`_ is a dataset with known chi2 fit results.
I have converted the information from the text file to
a python class for easier access:

.. literalinclude:: src/bb.py

.. _BoxBOD: http://www.itl.nist.gov/div898/strd/nls/data/LINKS/DATA/BoxBOD.dat


Results
+++++++

.. literalinclude:: output/bb/scipy_curve_fit.txt
.. literalinclude:: output/bb/lmfit.txt
.. literalinclude:: output/bb/minuit.txt
.. literalinclude:: output/bb/sherpa.txt
