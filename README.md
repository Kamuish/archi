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


 [1] There is no correction for cross-contamination between stars
 
 [2] If we have data in the entire 200*200 region (not expected to happen) and using the "dynam" mask for the background stars it might "hit" one of the edges of the image. In such case, larger masks will not increase in the direction in which the edge is reached. However, the mask can still grow towards the other directions, leading to masks significantly larger than the original star. In such cases, we recommend to manually change the mask size on the "optimized factors" file.
