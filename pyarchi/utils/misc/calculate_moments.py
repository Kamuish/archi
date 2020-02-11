import numpy as np
from cv2 import findContours, moments, threshold


def calculate_moments(bg_grid, img):
    """
    Apply image moments, as described in `OpenCv docs <https://docs.opencv.org/3.4.2/dd/d49/tutorial_py_contour_features.html>`_

    This functions pre-processes the image before calculating the moments, so that it conforms to OPenCv's input data types.   
    Parameters
    ----------
    bg_grid : int
        Size of the background grid
    img : np.array
        Image to be processed
    
    Returns
    -------
    centers
        Position of each detected star
    distances
        Distance of each star to the image center -> position [100,100]
    """

    scaling_factor = bg_grid / 200 if bg_grid else 1
    im = img.copy()
    im /= np.nanmax(im)
    im *= 255
    im = np.uint8(im)
    _, thresh = threshold(im, 10, 255, 0)
    contours, _ = findContours(thresh, 1, 2)

    new_cont = []
    for j in reversed(contours):  # removes small contours
        if len(j) > 10:
            new_cont.append(j)
    contours = new_cont
    del new_cont
    centers = []
    distances = []

    center = [100, 100]
    if bg_grid != 0:
        center = np.multiply(center, scaling_factor) + np.floor(scaling_factor / 2)

    for j in range(len(contours)):
        M = moments(contours[j])

        cY = M["m10"] / M["m00"]
        cX = M["m01"] / M["m00"]

        centers.append([cX, cY])
        distances.append(np.sqrt((cX - center[0]) ** 2 + (cY - center[1]) ** 2))

    return centers, distances
