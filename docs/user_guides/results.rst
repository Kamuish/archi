.. _outputs:

Structure of the outputs 
============================

There are two different ways to get access to the data extracted from the images: from the  :class:`~pyarchi.data_objects.Data.Data` object or
from the files that are written to the disk, with the :py:func:`~pyarchi.output_creation.storage_handler.store_data` function.



In memory
---------------

In order to access the data in memory, one can refer to the  :class:`~pyarchi.data_objects.Data.Data` documentation and  :class:`~pyarchi.data_objects.Star_class.Data`,
thus being able to find all that is necessary.

In Disk
--------------

There are two possible ways of storing data on disk: we either store data as  a text file, whose structure does not allow for proper organization of the data, or a  	
fits file. We shall now look into the structure of each one of them. 
    

Text file 
^^^^^^^^^^^^^^


.. automodule:: pyarchi.utils.data_export.export_txt
    :members:
    
Fits file 
^^^^^^^^^^^^^^

.. automodule:: pyarchi.utils.data_export.export_fits
    :members:
    