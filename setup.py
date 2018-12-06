from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='cmdprogress',
    version='1.1',
    author='Lucian Cooper',
    url='https://github.com/luciancooper/cmdprogress',
    description='Command Line Progress Bars',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='progress bar utility',
    license='MIT',
    packages=['cmdprogress'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
