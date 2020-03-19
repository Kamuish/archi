import glob
import re
import os 

def path_finder(mode, off_curve=None, **kwargs):
    """
    Searches inside the base folder for the desired files

    Parameters
    ----------
    mode:
        - subarray: retrieves the subarray file path
        - default: default lightcurve
        - stars : path for the Star catalogue file
    kwargs:
        - config values

    Returns
    -------

    """
    if mode == "subarray":

        possible_paths = glob.glob(os.path.join(kwargs["base_folder"], r"*eduction*/COR/**"))
        regex_patern = re.compile(r"\S+_Sub\S+.fits")

    elif mode == "default":
        possible_paths = glob.glob(os.path.join(kwargs["base_folder"], r"*eduction*/PHE/**"))
        curve_2_search = kwargs["official_curve"] if not off_curve else off_curve
        regex_patern = re.compile(r"\S+{}\S+.fits".format(curve_2_search))


    elif mode == "stars":
        possible_paths = glob.glob(os.path.join(kwargs["base_folder"], r"CH_*/data/**"))

        regex_patern = re.compile(r"\S+Star\S+.fits")

    return list(filter(regex_patern.findall, possible_paths))[0]