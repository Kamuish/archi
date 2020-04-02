import numpy as np 
import cv2 
from pyarchi.utils import calculate_moments

def get_contours(image):
    """
     This functions pre-processes the image before calculating the moments, so that it conforms to OPenCv's input data types.
    Removes masks with less than 50 pixels inside it
    Parameters
    ----------
    image : np.ndarray
        Image to study
    

    Returns
    -------
    found_masks
        List with all of the detected contours
    brightness
        Maximum flux value within the contours
    """

    im = image.copy()
    im /= np.nanmax(image)
    im *= 255
    im[np.where(im > 255)] = 255
    im[np.where(im <0)] = 0
    im = np.uint8(im)

    # TODO: change this threshold
    _, thresh = cv2.threshold(im, 10, 255, 0)
    contours, _ = cv2.findContours(thresh, 1, 2)

    to_remove = []
    for j in range(len(contours)):  # removes small contours (under 50 points)
        #print(cv2.contourArea(cont))

        if cv2.contourArea(contours[j]) <= 50:
            to_remove.append(j)
    for rm in reversed(to_remove):
        contours.pop(rm)

    found_masks = []
    brightness = [] 

    for cont in contours:
        mask = np.zeros(im.shape)
        cv2.drawContours(
            mask, [cont], -1, (255, 255, 255), -1
        )  # fills the contour with data

        mask[np.where(mask != 0)] = 1  # makes sure that we have binary mask
        found_masks.append(mask)
        brightness.append(np.nanmax(mask*image))

    return found_masks, brightness


def shape_analysis(image, bg_grid, repeat_removal = 0):

    masks_to_keep = []
    masks_locs = []

    all_masks, brightness = get_contours(image)

    for k in range(repeat_removal):
        index = np.argmax(brightness)
        if k ==0:
            im = image.copy()

        maximum_mask = all_masks[index]
        masks_to_keep.append(maximum_mask.copy())
        masks_locs.append(calculate_moments(maximum_mask, bg_grid))
        maximum_mask = shape_increase(maximum_mask, 7)

        im[np.where( maximum_mask == 1 )] = np.nan 

        all_masks, brightness = get_contours(im)

    scaling_factor = 1
    for mask in all_masks:
        locs = calculate_moments(mask, bg_grid)
        use = True
        for previous_locs in masks_locs:
            if np.isclose(previous_locs[0], locs[0], atol=15 * scaling_factor) and np.isclose(previous_locs[1], locs[1], atol=15 * scaling_factor):
                use = False 
        
        if use:
            masks_to_keep.append(mask)
            masks_locs.append(locs)
            
    return masks_to_keep, masks_locs


