#!/usr/bin/env python
"""Check Python / Cython / IPython installation and Python packages

Usage: ./check-python.py
"""

import sys

def sh(cmd):
    """Execute command in a subshell, return stdout and stderr"""
    from subprocess import check_output, STDOUT
    output = check_output(cmd, stderr=STDOUT, shell=True)
    return output.strip()

def check_python():
	"""Check which Python is used"""
	print('python executable:  %s' % sh('which python'))
	print('python version:     %s' % sh('python --version 2'))


def check_ipython():
	"""Check which ipython is used"""
	print('ipython executable: %s' % sh('which ipython'))
	print('ipython version:    %s' % sh('ipython --version'))


def check_cython():
	"""Check which Cython and compiler are used"""
	print('cython executable:  %s' % sh('which cython'))
	print('cython version:     %s' % sh('cython --version'))
	# @todo: Check complier used by Cython


def check_package(package_info):
	"""Gather info on one given package and return it in a dict"""
	name = package_info['name']
	try:
		exec('import %s' % name)
		package_info['importable'] = 'yes'
		package_info['version'] = eval('%s.__version__' % name)
		package_info['path'] = eval('%s.__path__[0]' % name)
	except ImportError:
		package_info['importable'] = 'no'
		package_info['version'] = ''
		package_info['path'] = ''
	return package_info


def check_packages():
	"""For each python package we use, check if it can be imported,
	and if so, where it is installed and what it's version is."""
	format_string = '{name:13} {importable:6} {version:18} {path}'
	names = ['numpy', 'scipy', 'pandas', 'lmfit']

	header_entries = dict(name='Package', importable='Import',
		version='Version', path='Path')
	print(format_string.format(**header_entries))
	print('-' * 80)
	for name in names:
		package_info = dict(name=name)
		check_package(package_info)
		print(format_string.format(**package_info))


if __name__ == '__main__':
	print('')
	check_python()
	check_ipython()
	check_cython()
	print('')
	check_packages()
	print('')
