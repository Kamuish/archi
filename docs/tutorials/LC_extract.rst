Tutorials
====================

.. _LC_extract:

How to extract Light Curves
--------------------------------

Assuming that the user has already applied the official Data Reduction pipeline over the data set that is to be studied 
and that the desired configurations have been already chosen, as specified in  Section :ref:`configyaml`  , one only has to run the following code,
to get light curves from all of the stars. 


.. code:: python

    from pyarchi import Photo_controller, store_data

    controller = Photo_controller(job_number = 1,
                                 config_path="<path_to_file>/config.yaml"
                                 )
    controller.optimize()  # not needed if the optimization process has already been done
    data_fits = controller.run()

    store_data(data_fits, job_number = 1, **controller.parameters)


Furthermore, if we want to change the configuration parameters of archi without having to edit the configuration file, we can do the following:


.. code:: python 

    from pyarchi import Photo_controller, store_data

    controller = Photo_controller(job_number = 1,
                                 config_path="<path_to_file>/config.yaml"
                                 )

    configs_override = {'base_folder': "<new_path>",
                        "grid_bg": 0,
                        "initial_detect": 'dynam',
                        "method": "shape",
                        "detect_mode": "dynam",
                        "optim_processes": n_tasks,
                        "val_range": [1, 10],
                        "low_memory":0,
                        "fine_tune_circle":1,
                        "optimize":0,
                        'uncertainties': 1,
                        'CDPP_type': "K2",
                        "debug": 1,
                        "plot_realtime": 0,
                        'repeat_removal': 0}
                        
    # we can override all parameters from the file. Typically, one only needs to change these

    controller.change_parameters(configs_override) 
    data_fits = controller.run()

    store_data(data_fits, job_number = 1, **controller.parameters)

If we had a data set with bright and faint stars, we would have to change the "repeat_removal" parameter, to remove the brighter regions in the image. 
It is recommended to avoid more than 2 iterations, as using larger values may start recognizing regions of the background as stars. 

In order to understand the organization of data inside the "data_fits" objects and the data that is stored with the "store_data" function, please
refer back to Section :ref:`outputs`.


It is **highly recommended** that the user builds its own routine to estimate the noise in the lightcurve. To do so, a given metric must be passed in the configs_override 
 This metric will be minimized during the mask selection routine. The current version only gives the user the flux and observation time.

.. code:: python 

    from pyarchi import Photo_controller, store_data

    controller = Photo_controller(job_number = 1,
                                 config_path="<path_to_file>/config.yaml"
                                 )
    def noise_metric(flux, time):
        metric = np.std(flux)
        return metric
    configs_override = {'CDPP_type': noise_metric}


How to plot the outputs
--------------------------------

By default archi creates some plots, that are stored in the created folders, containing information of the light curves from
each star and by comparing the target one against the DRP.

However, if we want to do so manually, we can do it this way:

.. code:: python 

    from pyarchi import Photo_controller, store_data
    import matplotlib.pyplot as plt 

    controller = Photo_controller(job_number = 1,
                                 config_path="<path_to_file>/config.yaml"
                                 )
    controller.optimize()  # not needed if the optimization process has already been done
    data_fits = controller.run()

    for star in data_fits.stars: # iterate through all of the stars 
        plt.plot(data_fits.mjd_time, star.photom)
        plt.title(f"{star.name}")
        plt.xlabel("MJD time [days]")
        plt.ylabel("Flux [ADU]")
        plt.show()

In order to better understand what information one can get from the controller, stars and data_fits, please refer back to relevant documentation.
