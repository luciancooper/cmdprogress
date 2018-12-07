from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='cmdprogress',
    version='1.2',
    author='Lucian Cooper',
    url='https://github.com/luciancooper/cmdprogress',
    description='Command Line Progress Bars',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='progress bar utility',
    license='MIT',
    packages=['cmdprogress'],
    install_requires=[
        'colorama;platform_system=="Windows"'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
