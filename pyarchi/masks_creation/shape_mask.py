import cv2
import numpy as np

from pyarchi.data_objects.Mask import logger


def create_shape_mask(im, stars, increase_factor, scaling_factor, primary, secondary):
    """
    Finds the contours of the image, with openCv default functions

    Parameters
    ----------
    im:
        copy of the image used for the shape detection
    stars:
        list of all the  :class:`pyarchi.star_track.Star_class.Star` objects

    increase_factor:
        Number of pixels added to the outside of the shape. For example, if factor = 1 then we add a layer of pixels
        around the entire shape

    size_grid_change:
        SIze of the background grid in use

    primary:
        Methodology to apply to the central star. If it's dynam then the initial position of that star is changed to
        be the one determined here.
    secondary:
        Methodology to apply to the outer stars. If it's dynam then the initial position of those stars are changed to
        be the ones determined here.

    Returns
    -------
    masks_dict:
        Dictionary where the keys are the number of the star and the values the corresponding mask
    """

    if primary != "shape" and secondary != "shape":
        return {}

    to_calculate = []
    if primary == "shape":
        to_calculate.append(0)

    if secondary == "shape":
        to_calculate = to_calculate + [star.number for star in stars[1:]]

    # Normalization to use with OpenCv
    im /= np.nanmax(im)
    im *= 255
    im = np.uint8(im)

    # TODO: change this threshold
    _, thresh = cv2.threshold(im, 10, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)

    to_remove = []
    for j in range(len(contours)):  # removes small contours (under 5 points)
        if len(contours[j]) <= 11:
            to_remove.append(j)
    for rm in reversed(to_remove):
        contours.pop(rm)
    
    if len(contours) != len(stars):  # we need to have the same number of masks and stars
        logger.fatal("Number of detected contours and stars does not add up")
        logger.fatal(" \t Contours: {}; Stars:{}".format(len(contours),len(stars)))

        return -1

    mask_dict = {}
    for cont in contours:
        mask = np.zeros(im.shape)
        cv2.drawContours(
            mask, [cont], -1, (255, 255, 255), -1
        )  # fills the contour with data

        mask[np.where(mask != 0)] = 1  # normalizes the array

        for index, star in enumerate(stars):
            if index not in to_calculate:
                continue
            pos = star.init_pos.copy()

            if mask[int(round(pos[0])), int(round(pos[1]))] != 0:
                # since the contours are not ordered like the stars one must check if we have data from the contours in
                # the specified position

                if isinstance(increase_factor, (np.int64, int)):
                    final_mask = shape_increase(mask, increase_factor)
                else:
                    final_mask = shape_increase(mask, increase_factor[str(star.number)])
                mask_dict[index] = final_mask

    return mask_dict

