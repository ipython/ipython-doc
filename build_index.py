#!/usr/bin/env python
"""run rest with stylesheet, and filter to add the logo in the header."""
from subprocess import Popen, PIPE, CalledProcessError, check_call

def sh2(cmd):
    """Execute command in a subshell, return stdout.

    Stderr is unbuffered from the subshell.x"""
    p = Popen(cmd, stdout=PIPE, shell=True)
    out = p.communicate()[0]
    retcode = p.returncode
    if retcode:
        raise CalledProcessError(retcode, cmd)
    else:
        return out.rstrip()

autotitle='<h1 class="title">IPython</h1>'
logotitle='<h1 class="title"><a href="http://github.com/ipython"><img src="logo-50.png" id="logo"/>IPython</a></h1>'

def main():
    html = sh2('rst2html.py index.rst --stylesheet style.css -q')
    html = html.replace(autotitle, logotitle)
    with open('index.html', 'w') as f:
        f.write(html)

if __name__ == '__main__':
    main()