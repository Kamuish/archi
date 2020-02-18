""" 
CHEOPS mission, one of ESA’s mission has been launched in December 2019. Around the same date, the official pipeline, DRP, was also announced
The DRP only works for the target star, thus leaving a 
lot of information left to explore. Furthermore, the presence of background stars in our images can mimic astrophysical signals in the target star.

We felt that there was a need for a pipeline capable of analysing those stars and thus, built archi, 
a pipeline built on top of the DRP, to analyse those stars. Archi has been tested with simulated data,
showing proper behaviour. ON the target star we found photometric precisions either equal or slightly better than the DRP.
For the background stars we found photometric preicision 2 to 3 times higher than the target star.
"""


from setuptools import setup
from setuptools import find_packages
import os 

DOCLINES = (__doc__ or '').split("\n")
setup(name='pyarchi',
      version='1.0.1',
      description='archi - pipeline to study CHEOPS background stars',
      url='http://github.com/Kamuish/archi',
      author='Kamuish',
      long_description="\n".join(DOCLINES),
      author_email='amiguel@astro.up.pt',
      license='GNU General Public License v3.0',
      packages=find_packages(), 
      zip_safe=False,
      classifiers=[
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8'
      ]
      
      )
