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

    data_fits = controller.run()

    store_data(data_fits, job_number = 1, **controller.parameters)


In order to understand the organization of data inside the "data_fits" objects and the data that is stored with the "store_data" function, please
refer back to Section :ref:`outputs`.