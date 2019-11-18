# ARCHI - An expansion to the CHEOPS mission official pipeline

With the CHEOPS mission launch date set for later this year, in October/November, the official
Data Reduction Pipeline (DRP) has been unveiled. The official pipeline only works for the
target star, thus leaving a lot of information to explore. In this work we present archi, a pipeline
built on top of the DRP, to analyse those stars. We found that this pipeline allows us to extract
light curves from background stars in CHEOPS images, albeit with an higher noise value than
the light curves produced for the central star. Our detection routines are able of detecting all
of the visibly seen stars in the image, assuming that none of the stars are not saturated, which
should be the standard observational case.
