.. _configyaml:

Configuration
================

In order to configure the behavior of the pipeline, one has to edit the configuration.yaml
file, shown `in here <https://github.com/Kamuish/archi/blob/master/configuration_files/example_config_file.yaml>`_ .

Even though everything can be configured throughout this file, it's also possible to change any parameter from within
python, as described in :ref:`photo_controller`. Before the routines start, the passed parameters
are subjected to an analysis, to insure that all of the previded data has the correct data types.


============================
General configurations
============================
* base_folder : 
    *   Path to the data folder, eg: "/home/Kamuish/data_files/CHEOPSim_job6201/"
* optimized_factors : 
    *   path to save and load the optimized "increase factors"

* official_curve: Uses one of the DRP's light curves to compare the results against our owns; The comparison is not made, if the debug parameter is set to zero.
    * OPTIMAL 
    * DEFAULT 
    * RSUP 
    * RINF

* method:  Format of the region in which the image will be analysed (for each star).
    *  "circle"  -> uses a circular opening around each star;
    *  "shape"   -> uses the contour of the star to create a mask


* initial_detect: How the centers are tracked
    *   fits : uses information from the Star Catalogue file, provided by the DRP
    *   dynam : uses image processing;

* detect_mode: How the stars are tracked
    * "static" - Extracts the inicial position from the FITS file and, for each frame, they are rotated by the difference of the rotation angle of the satellite;
    * "dynam" - in each image the contours are detected and the center of each is extrapolated using the contour's moments;
    * "offsets" - uses the "static" process and afterwards calculates the corrections for the center star position and applies it to all the points.

* uncertainties
    *    Enable the calculation of the uncertainties

* grid_bg:  
    *   Size of the grid used for improved resolution. If it's set to zero then no background grid is used. Otherwise, it needs to be a multiple of the image's sizes (200 px)


* optimize: 
    *   If it's 1 then the data files will be pre-processed to find the optimal radius, i.e. , the radii that minimizes the dispersion for each star; If it's 0 the radii used will be the ones from the optimized_radius.json file

* optimization_extensions: 
    * number of times that the optimization process is expanded

* optim_processes:
    * Number of cores to use for the optimization process. if it's running on a laptop, it's recommended to use 2 or 3

* fine_tune_circle: 
    *   fine search for the mask best size. The step keyword has no effect over this process

* val_range: 
    *   values that the mask size can take; used in the optimization process

* step:
    * Step between mask sizes for the optimization process. Recommended to be 1


* headless: 
    * Is the code running on a headless server

* low_memory: 
    * Activate low memory mode. Recommended to be active when working with the background grids or larger data sets.

* CDPP_type: Which noise metric to use;
    * K2
    * CDPP

* debug: 
    *   If it's 1 then we will have a comparison between the data obtained using this method and the one from the official pipeline. THis comparison is only done for the center star, since the official pipeline does not work for the outer stars.


* plot_realtime: 
    *   If it's 1 we will see the images with the region under study marked with a circle. When it's set to 1 the program shows a performance hit since the plot uses up some computational power. If the optimize parameter is set to 1 this one is set to 0 during the optimization process.

* show_results: 
    *   Shows the photometric curve of each star

* export_text: 
    *   export the lightcurve of the central star to a text file, including the MJD_TIME and ROLL_ANGLE

* export_fit : 
    *   export, to  FITS file, the photometric curves of all stars, calibration information and the relevant configuration values.



