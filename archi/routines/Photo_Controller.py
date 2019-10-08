import yaml

from .photometric_process import photometry
from archi.data_objects import Data

from archi.utils import general_optimizer, store_optimized_radius
from archi.utils import create_logger, parameters_validator

logger = create_logger("Photo Controller")


class Photo_controller:
    """
        Controller class that allows an easy interface with all the important functions in the module
    """

    def __init__(self, job_number, config_path="configs/config.yaml", no_optim=False):
        self.job_number = job_number
        logger.info("Loading Parameters:")

        if isinstance(config_path, str):
            with open(config_path, "r") as stream:
                kwargs = yaml.load(stream)
        else:  # we can pass a dict
            kwargs = config_path

        self.kwargs = kwargs
        if no_optim:
            self.kwargs["optimize"] = 0

        if self.kwargs[
            "optimize"
        ]:  # Finds the best factors to minimize Cv and updates the json file
            self.__optimize()

        self._completed_run = False

    def _check_parameters(func):  # pylint: disable=no-self-argument
        """
        Used to validate the error flag before running a function.
        Decorator used inside this class

        Returns
        -------

        """

        def on_call(self, *args, **kwargs):

            if (
                func.__name__ == "run" and self.kwargs["optimize"]
            ):  # pylint: disable=no-member
                pass
            else:
                wrong_params, warnings, kwargs = parameters_validator(**self.kwargs)
                if any(warnings):
                    logger.fatal("\t Found Warnings: {}".format(len(warnings)))
                    [logger.fatal("\t \t" + warn) for warn in warnings]

                if any(wrong_params):
                    logger.fatal(
                        "Problem with the passed parameters. Process is going to stop now"
                    )
                    logger.fatal("\t Bad parameters: {}".format(len(wrong_params)))
                    [logger.fatal("\t \t" + wrong_param) for wrong_param in wrong_params]
                    return -1
            if func.__name__ == "__optimize": # pylint: disable=no-member
                return func(self)  # pylint: disable=not-callable
            else:
                return func(self, *args, **kwargs) # pylint: disable=not-callable

        return on_call

    @_check_parameters
    def run(self, data_fits, factor=None, **kwargs):
        """
        Calls the main method to run the star analysis pipeline

        Parameters
        ----------
        data_fits:
            :class:`archi.main.initial_loads.Data`  object with all the stars information inside
        factor
            Used for the optimization process. During normal functioning process then so value should be passed
        kwargs
            Config values, retrieved from the file on the class initialization
        Returns
        -------

        """

        configs = (
            self.kwargs if (factor is None and not self.kwargs["optimize"]) else kwargs
        )
        result = data_fits.load_parameters(factor, **configs)

        if result == -1:
            logger.fatal("Critical error")
            return data_fits
        self.data_fits = photometry(data_fits, **configs)

        if not self.kwargs["optimize"]:
            logger.warning("Checking for out of bounds masks:")
            for star in self.data_fits.stars:
                if star.out_bound:
                    logger.warning("\t \t Star {} is out of bounds".format(star.number))

        if self.data_fits.abort_process:
            logger.fatal("Problems were found. Could not run properly !!!!!")
            raise Exception("Something went wrong")

        self._completed_run = True

        return self.data_fits

    def change_parameters(self, params_dict):
        """
        Updates the kwargs with new values. A dictionary is passed in, with keys corresponding to parameters and each
        value it's the new configuration for that specific parameter.
        At this stage no validation is made over the passed values. Such validation occurs before the routines,
         to make sure that the correct parameters were added.

        Parameters
        ----------
        params_dict:
            Dictionary with the values that we wish to change

        Returns
        -------

        """
        new_dict = self.kwargs.copy()
        for key, value in params_dict.items():
            if key not in self.kwargs:
                raise AttributeError(
                    "The {} configuration value does not exist".format(key)
                )
            new_dict[key] = value

        self.kwargs = new_dict

    def optimize(self):
        """
        Run the optimization routine without instantiating a new object.
        Returns
        -------

        """
        self.kwargs["optimize"] = 1  # just making sure
        self.__optimize()

    @_check_parameters
    def __optimize(self):
        """
        Optimization process. Called when the class is initialized
        Returns
        -------

        """
        import time

        t0 = time.time()
        logger.info("Starting optimization process")

        vals = general_optimizer(
            self.run,
            data_f=Data(),
            job_number=self.job_number,
            max_process=self.kwargs["optim_processes"],
            **self.kwargs
        )

        logger.info("Optimization process completed after {} s".format(time.time() - t0))
        self.kwargs["optimize"] = 0

        if store_optimized_radius(vals, **self.kwargs) == -1:
            logger.critical("Problems were found. Failed to save optimized values.")
            return
        del vals
        self._completed_run = False

    @property
    def parameters(self):
        return self.kwargs
