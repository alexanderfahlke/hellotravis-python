# -*- coding: utf-8 -*-

import os
import sys

try:
    # Use setuptools if available, for install_requires (among other things).
    import setuptools
    from setuptools import setup
except ImportError:
    setuptools = None
    from distutils.core import setup

base_dir = os.path.dirname(os.path.abspath(__file__))
kwargs = {}
version = "0.1.0"
package_dir = "hellotravis-python"

if setuptools is not None:
    # If setuptools is not available, you're on your own for dependencies.
    install_requires = []
    tests_require = []
    if sys.version_info < (2, 7):
        install_requires.append('pytz')
        tests_require.append("unittest2")
    if sys.version_info < (3, 5):
        install_requires.append('pytz')
        tests_require.append("unittest2")
    kwargs['install_requires'] = install_requires
    kwargs['tests_require'] = install_requires

if sys.argv[-1] == 'publish':
    os.system("git tag -a %s -m 'v%s'" % (version, version))
    print("Published version %s, do `git push --tags` to push new tag to remote" % version)
    sys.exit()


def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == "":
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

packages = []
for dirpath, dirnames, filenames in os.walk(package_dir):
    # ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith("."):
            del dirnames[i]
    if "__init__.py" in filenames:
        packages.append(".".join(fullsplit(dirpath)))

setup(
    name="hellotravis-python",
    version=version,
    description="A repository for testing stuff with python, travis-ci and coveralls",
    long_description="\n\n".join([
        open(os.path.join(base_dir, "README.md"), "r").read(),
        open(os.path.join(base_dir, "CHANGELOG.md"), "r").read()
    ]),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        ],
    url="http://github.com/alexanderfahlke/hellotravis-python",
    author="Alexander Fahlke",
    author_email="alexander.fahlke@gmail.com",
    maintainer="Alexander Fahlke",
    maintainer_email="alexander.fahlke@gmail.com",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    packages=packages,
    zip_safe=False,
    test_suite="hellotravis-python.test.get_tests",
    **kwargs
)
