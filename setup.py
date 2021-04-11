import setuptools
import re

NAME = "py2cozy"
VERSIONFILE=NAME+"/_version.py"

verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

    
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=NAME,
    version=verstr,
    author="tintinmar1995",
    author_email="martin.masson@protonmail.com",
    description="Very personal tool to use my cozy very personal cloud",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tintinmar1995/py2cozy",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose']
)
