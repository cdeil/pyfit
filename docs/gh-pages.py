#!/usr/bin/env python
"""
Script to commit the doc build outputs into the github-pages repo.
Use: gh-pages.py
"""

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import sys
import os
import subprocess

#-----------------------------------------------------------------------------
# Globals
#-----------------------------------------------------------------------------

pages_dir = 'gh-pages'
html_dir = '_build/html'
pdf_dir = '_build/latex'
pages_repo = 'git@github.com:pyfit/pyfit.github.com.git'

def sh(cmd):
    """Execute command in a subshell, return status code."""
    print '=== Executing command: ', cmd
    return subprocess.check_call(cmd, shell=True)

def cd(path):
    print '=== Changing directory to:', path
    return os.chdir(path)

if __name__ == '__main__':
    
    start_dir = os.getcwdu()

    if not os.path.exists(pages_dir):
        # Check out pages_repo in pages_dir
        sh("git clone %s %s"%(pages_repo, pages_dir))
    else:
        # Update pages_repo in pages_dir
        cd(pages_dir)
        sh('git pull')
        cd(start_dir)

    # Nuke everything in pages_dir
    sh('rm -rf %s/*' % pages_dir)

    # Copy docs to pages_dir
    sh('cp -r _build/html/* %s' % pages_dir)

    # Commit new docs
    try:
        cd(pages_dir)

        sh('git add -A')
        try:
            sh('git commit -m "Updated doc release"')
            print
            print 'Most recent 3 commits:'
            sys.stdout.flush()
            sh('git --no-pager log --oneline HEAD~3..')
        except subprocess.CalledProcessError:
            print 'INFO: Nothing changed. No need to commit.'
            sys.exit()
    finally:
        cd(start_dir)

    # Push is not done automatically.
    # to have a chance to check if something went wrong.
    print
    print 'INFO: Now verify the build in: %r' % pages_dir
    print "INFO: If everything looks good, 'git push'"
