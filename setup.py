import sys
from setuptools import setup, find_packages


# Remove current dir from sys.path, otherwise setuptools will peek up our
# module instead of system's.
sys.path.pop(0)
sys.path.append(".")
import sdist_upip  # NOQA

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='micropython-ljus',
    version="0.0.1",
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
