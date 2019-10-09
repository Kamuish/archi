Tutorials
====================

.. _LC_extract:

How to extract Light Curves
--------------------------------

.. code:: python

    from archi import Photo_controller, store_data

    controller = Photo_controller(job_number = 1,
                                 config_path="<path_to_file>/config.yaml"
                                 )

    data_fits = controller.run()

    store_data(data_fits, job_number = 1, **controller.parameters)