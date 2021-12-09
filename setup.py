import codecs
import os.path
import sys
from setuptools import setup, find_packages


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
sys.path.append(".")
import sdist_upip  # NOQA

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='micropython-ljus',
    version=get_version('src/ljus/__init__.py'),
    license='MIT',
    author='Linus Törngren',
    author_email='linus@etnolit.se',
    description="A MicroPython package for LEDs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Limpan/micropython-ljus',
    cmdclass={'sdist': sdist_upip.sdist},
    project_urls={
    'Bug Tracker': 'https://github.com/Limpan/micropython-ljus/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
        "Topic :: Multimedia",
    ],
    package_dir={"": 'src'},
    packages=find_packages(where="src"),
    python_requires=">=3.4",
)
