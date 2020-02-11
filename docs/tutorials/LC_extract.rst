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

    configs_override = {'base_folder': "/home/amiguel/archi/data_files/CHEOPSim_job7796/",
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
                        'CDPP_type': "DRP",
                        "debug": 1,
                        "plot_realtime": 0}

    controller.change_parameters(configs_override) # we can overrid all parameters from the file. Typically, one only needs to change these

    data_fits = controller.run()

    store_data(data_fits, job_number = 1, **controller.parameters)


In order to understand the organization of data inside the "data_fits" objects and the data that is stored with the "store_data" function, please
refer back to Section :ref:`outputs`.


How to plot the outputs
--------------------------------

By default archi creates some plots, that are stored in the created folders, containing information of the light curves from
each star and by comparing the target one against the DRP.

However, if we want to do so manually, we can:

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

