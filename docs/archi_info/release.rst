What is new in archi
===========================
v1.2.1 (Current)
-----------------------
* Bug Fixes:
    #. No images were stored when a gif was set to be created
    #. Missing imageio in the requirements.txt

v1.2.0 (Current)
-----------------------
* New Features:
    #. Allow the user to provide a custom metric for the lightcurve noise
* Bug Fixes:
    #. removed critical bug when evaluating old keyword
    
v1.1.0 
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