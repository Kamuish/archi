[![Documentation Status](https://readthedocs.org/projects/archi/badge/?version=latest)](https://archi.readthedocs.io/en/latest/?badge=latest)
# ARCHI - An expansion to the CHEOPS mission official pipeline

CHEOPS mission, one of ESA's mission has been launched in December 2019. 

The official pipeline released for this mission only works for the
target star, thus leaving a lot of information  left to explore. Furthermore, the presence of background stars in our images
can mimic astrophysical signals in the target star. 


We felt that there was a need for a pipeline capable of analysing those stars and thus, built archi, a pipeline
built on top of the DRP, to analyse those stars. Archi has been tested with simulated data, showing proper behaviour.
ON the target star we found photometric precisions either equal or slightly better than the DRP. For the background stars we found photometric preicision 2 to 3 times higher than the target star.

# How to install archi 

The pipeline is written in Python3, and most features should work on all versions. However, so far, it was only tested on python 3.6, 3.7 and 3.8

To install, simply do :

    pip install pyarchi

# How to use the library 

A proper introduction to the library, alongside documentation of the multiple functions and interfaces can be found [here](https://archi.readthedocs.io/en/latest/)


# Known Problems

 [1] The normalization routine fails if one of the stars is saturated; Since the images are normalized in relation to their brigthest point, the saturation of a star leads to us being unable to detect faint stars (under a given magnitude threshold)
 
 [2] There is no correction for cross-contamination between stars
