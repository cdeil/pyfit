
.. _installation:

Installation
============

Unfortunately installing Python packages is often hard. So if you only have little time we suggest you only read the documentation and rendered IPython notebooks on these web pages. If you do want to do modelling and fitting with Python, read on.

.. _getting_started_getting_pyfit:

Getting pyfit
-------------

You can get pyfit from `github <https://github.com/pyfit/pyfit>`_ either by downloading a `ZIP file <https://github.com/pyfit/pyfit/archive/master.zip>`_ or by cloning the `git <http://git-scm.com>`_ repository.

If you did get the zip file, execute these commands in a terminal::

	$ cd <to where the zip file is>
	$ unzip pyfit-master.zip # this might have been done automatically by your browser or operating system
	$ cd pyfit-master/notebooks

To clone the git repo::

	$ git clone https://github.com/pyfit/pyfit.git
	$ cd pyfit/notebooks

The advantage of the git repo is that you can easily update via `git pull <http://git-scm.com/docs/git-pull>`_ and contribute back bug fixes and additions.

.. _getting_started_running_ipython_notebooks:

Running the IPython notebooks
-----------------------------

Execute this command to start the ipython notebook in the ``notebooks`` folder::

	$ ipython notebook --pylab=inline
	...
	[NotebookApp] The IPython Notebook is running at: http://127.0.0.1:8890/
	[NotebookApp] Use Control-C to stop this server and shut down all kernels.

Your default web browser should open a page displaying a list of notebooks. Clicking on one will start that notebook in a separate tab.

Note that you are seeing the notebook as executed on the pyfit developer machines, the notebook did not yet execute on your computer. To execute a given cell select it and type ``Shift + Enter``. To execute the whole notebook in order select ``Cell -> Run All`` from the menu at the top.

IPython notebooks are wonderful interactive environments for coding and fitting. Feel free to play with the existing examples to learn or start a new notebook for your actual data analysis task.

The shell where you executed ``ipython notebook --pylab=inline`` can't be used until you shutdown the notebook (e.g. by typing ``CTRL + C`` and ``y + ENTER`` toconfirm to exit). If you need a new shell, just open another one and leave this one alone.

Troubleshooting
+++++++++++++++

* If you get an error message from ``ipython notebook --pylab=inline`` you don't have IPython installed or your installation is broken. In that case you have to fix this first, see `Installing the Python fitting package and their dependencies`_ below for links with instructions.
* On some systems the web browser doesn't open automatically, in that case open it yourself and direct it to the URL ``http://127.0.0.1:8890/`` mentioned in the terminal.
* If you don't see any notebooks, make sure you executed ``ipython notebook --pylab=inline`` in the ``pyfit/notebooks`` folder, e.g. by using executing the ``pwd`` or ``ls -lh`` commands.
* If you ever get an ``ImportError: No module named X`` for one of the example notebooks you probably don't have package ``X`` installed. See `Testing your installation`_ and `Installing the Python fitting package and their dependencies`_.
* Sometimes a package is installed, but your shell is not configured correctly to use it. Then you typically need to add some folder to your ``PATH``, ``PYTHONPATH`` or ``LD_LIBRARY_PATH`` shell environment variables, or execute a command like ``source setup_package_X.sh`` that will setup your shell to use package ``X`` for you. We can't write instructions for all packages and operating systems here, if you can't resolve the issue by reading the package documentation, please contact their support forum or mailing list or ask on the pyfit mailing list.

Installing the Python fitting package and their dependencies
------------------------------------------------------------

Installing and updating all the packages we use and their dependencies one by one is way too much work. Instead you should use a package manager or a Scientific Python distribution. Here's some basic information on `Installing the Scipy Stack <http://scipy.github.com/install.html>`_


.. todo:: Some packages (Sherpa, RTMinuit, ...) are not available via package managers. We should add them there or give the commands to pip-install them here.

Python 2 or Python 3?
+++++++++++++++++++++

Currently the Python community is transitioning from Python 2 to Python 3 and you have to decide which one to use (see `Python2orPython3 <http://wiki.python.org/moin/Python2orPython3>`_ and `"History of Python" on Wikipedia <http://en.wikipedia.org/wiki/History_of_Python>`_).

This paragraph was writting in November 2012, hopefully in a few years everyone will be using Python 3, but for now, even though Python 3.0 was already released in 2008 and a month ago Python 3.3 was released, **our recommendation is that you use Python 2.7**, which was released in 2010 and is the last release in the Python 2 series.

The reason is simply that Python 3 adoption in the scientific computing field has been super slow (for reasons we won't go into here) and there are some Python modelling and fitting packages we use here that have not been ported to Python 3 yet (Sherpa, RTMinuit, TODO: others? list all.). For those that have been ported some are not available for Python 3 in the main package repositories yet and because there have been only few Python 3 users you are more likely to encounter bugs.

Actually thinking about it, almost all packages are ported to Python 3 and the biggest problem with Python 3 adoption at the moment is recommendations as the one above, so I'd like to add this recommendation:
**If you're young (say expecting to be still using Python three years from now) and not on a deadline to have your modelling and fitting done next Tuesday, do use Python 3** and report any issues you run into to the package developers. This way you are making the world a better place and won't have to make the switch to Python 3 next year. :-)

Mac
+++

* Install `XCode <https://developer.apple.com/xcode/>`_ , then start it, go to Preferences -> Downloads and click on Install for the XCode Command Line Tools. You can now close the XCode IDE (integrated development environment), the only reason we installed it because we need a C / C++ compiler, and `Mac OS X <http://www.apple.com/osx/>`_ is shipped without one.
* Install `Macports <http://www.macports.org>`_, a package manager you can use to easily install, update or uninstall most of the free open source data analysis software that exists (16,000 packages available in late 2012). Macport uses the `port` command, which e.g. has these (and many more) sub-commands::

    $ sudo port search <something you want> # to find packages
    $ sudo port info <package name> # get info on a package
    $ sudo port install <package name>
    $ sudo port selfupdate && sudo port upgrade outdated # update everything

* Should Macports drive you to drink you can try `Homebrew <http://mxcl.github.com/homebrew/>`_. This is their slogan, it's not my opinion that Homebrew is better. Actually I personally think (and I'm sure other's will disagree) Macports is simpler and less error-prone to install a scientific Python environment because Macports can install Python packages, whereas with Homebrew you have to use a second program such as `pip <http://www.pip-installer.org>`_ and generally installing, updating and uninstalling is harder.
* Open a terminal and enter the following command to download and install everything we need. You have to give your password. Sometimes packages are available as binaries, sometimes not. Typically this will take several hours and at parts use 100% of your CPU, so we recommend you do this before going to bed::

    $ sudo port install py27-numpy py27-scipy py27-matplotlib \
    py27-ipython +notebook py27-pandas py27-sympy py27-nose \
    TODO: add missing packages

Ubuntu and Debian
+++++++++++++++++

Execute this command. All packages are pre-compiled binaries, installation should take maybe an hour depending on your download and disk speed::

	$ sudo apt-get install python-numpy python-scipy python-matplotlib \
	ipython ipython-notebook python-pandas python-sympy python-nose \
	TODO: add missing packages, check IPython notebook version


Fedora and Scientific Linux
+++++++++++++++++++++++++++

.. todo:: give command here so that user doesn't have to look up all the exact package names.

Testing your installation
-------------------------

To check your installation run these commands::

	$ cd pyfit/tools  # or cd to wherever you put pyfit
	$ ./check-installed-packages.py
