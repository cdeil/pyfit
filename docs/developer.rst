Developer Information
=====================

How to process IPython notebooks?
---------------------------------

* Install https://github.com/ipython/nbconvert
* Don't forget to add the repo folder to your PATH (see nbconvert install instructions)

Every time you update a note book, do this:
* cd packages
* nbconvert.py sherpa.ipynb -f py
* nbconvert.py sherpa.ipynb -f rst
* mv 
* git commit TODO



How to build the documentation?
-------------------------------

To build the documentation use these commands:

	cd docs
	make gh-pages
	

http://cdeil.github.com/python_modelling_fitting.github.com/