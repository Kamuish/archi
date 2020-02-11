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

        x = glob.glob(os.path.join(kwargs["base_folder"], r"*eduction*/COR/**"))
        cc = " ".join(x)

        return re.compile(r"\S+_Sub\S+.fits").findall(cc)[0]

    elif mode == "default":
        x = glob.glob(os.path.join(kwargs["base_folder"], r"*eduction*/PHE/**"))
        cc = " ".join(x)

        curve_2_search = kwargs["official_curve"] if not off_curve else off_curve
        return re.compile(r"\S+{}\S+.fits".format(curve_2_search)).findall(cc)[0]

    elif mode == "stars":
        x = glob.glob(os.path.join(kwargs["base_folder"], r"CH_*/data/**"))

        cc = " ".join(x)
        return re.compile(r"\S+Star\S+.fits").findall(cc)[0]
