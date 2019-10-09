.. archi documentation master file, created by
   sphinx-quickstart on Tue Oct  8 19:24:33 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to archi's documentation!
=================================

This project is part of the work developped during my MSc's thesis, titled "An expansion to the
CHEOPS mission official pipeline".

In this project we proposed to expand the functionality of the CHEOPS mission official data
reduction pipeline (DRP), in a project named "An expansion foR the CHeops mission pipelIne - ARCHI
", to maximize the scientific gains from its operation.


.. toctree::
   :maxdepth: 1
   :caption: User Guide 

        Installation <user_guides/installation>
        Configuration <user_guides/configs>
        A quick overview <user_guides/overview>
        The User interface <user_guides/user_interface>
        The Optimization routine <user_guides/optimization>


.. toctree::
   :maxdepth: 2
   :caption: Tutorials

    Light curve extraction <tutorials/LC_extract>


.. toctree::
   :maxdepth: 1
   :caption: Developper Documentation


    Star operations <modules/stars>
    Mask definition process <modules/masks>
    The utility scripts <modules/utility>

    Outputs creation <modules/outputs>


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
