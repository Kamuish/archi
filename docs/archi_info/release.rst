What is new in archi
===========================

v1.1.0 (Current)
-----------------------
* New Features:
    #. Added the ability to store a gif of the star tracking routine
    #. Improved the logging of cases where archi fails
    #. If the *dynam* star tracking routine fails it uses the *static* routine to estimate the next point
    #. If the roll angle from the DRP fails (Nans instead of numbers) the *dynam* routine estimates the roll angle based on passed time between images. This is done allow the predictions to still be calculated

* Bug Fixes:
    * Removed bug where the multiple processes would stay open when the workers would raise an Exception


v1.0.0
--------
Original Version