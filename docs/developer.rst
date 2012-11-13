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


How to build the sphinx documentation?
--------------------------------------

To build the documentation use these commands:

	cd docs
	make gh-pages
	cd gh-pages
	git diff # review changes
	git push # if everything looks good

 `make gh-pages` makes the html documentation, and then calls `python gh-pages.py`.
 `gh-pages.py` copies it in gh-pages sub-folder and commits it there.
 It's pretty simple, read it to see exactly what it does.

There's a few ways of using gh-pages. We are using the master branch of the
http://github.com/pyfit/pyfit.github.com repo, i.e. "organization project pages" as described here:
https://help.github.com/articles/user-organization-and-project-pages

The new rendered docs should appear immediately at http://pyfit.github.com
If something is strange review the files and commits at http://github.com/pyfit/pyfit.github.com