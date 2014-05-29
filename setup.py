
from setuptools import setup, find_packages

setup(
    name='disabledoc',
    version='0.1.1',
    description="",
    long_description="""""",
    author='Nat Williams, Kumar McMillan, Gabriel Chang',
    author_email='gabe@nextdoor.com',
    license="Apache License",
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['Nose'],
    url='https://github.com/gabend/disable-docstring',
    include_package_data=True,
    entry_points="""
       [nose.plugins.0.10]
       disabledoc = disabledoc.plugin:DisableDocstring
       """,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Testing'
        ],
    )
