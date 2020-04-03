import cv2
import numpy as np
from pyarchi.utils import calculate_moments, shape_analysis


def create_predictions(Data_fits, img_number):
    """
    Rotates the points in the last know position by the corresponding rotation angle (difference between current angle
     and the one from the last image), predicting the next position of the star

    Parameters
    ----------
    Data_fits:
         :class:`pyarchi.main.initial_loads.Data` object.
    img_number:
         Number of the current image

    Returns
    -------

    """

    predicts = {}
    if img_number + 1 < len(Data_fits.roll_ang):
        fwd_im = Data_fits.roll_ang[img_number + 1]
        bck_im = Data_fits.roll_ang[img_number]

        rot_mat = Data_fits.get_rot_mat(((fwd_im - bck_im) * np.pi / 180), clockwise=True)

        for index in range(len(Data_fits.stars)):
            center = [100, 100]

            if Data_fits.bg_grid != 0:
                scaling_factor = Data_fits.bg_grid / 200
                center = np.multiply(center, scaling_factor) + np.floor(
                    scaling_factor / 2
                )

            pair = Data_fits.stars[index].positions[-1].copy()

            coords = np.dot(rot_mat, [[pair[0] - center[0]], [pair[1] - center[1]]])

            x = coords[0][0] + center[0]
            y = coords[1][0] + center[1]

            predicts[index] = [x, y]

    return predicts


def dynam_method(Data_fits, index, primary, secondary, repeat_removal):
    """
    This function is used to calculate the position of the center of each contour. In order to do that
    we calculate the moments of the image, which allows us to derive it's "center of mass".
    All contours with less than 7 points are discarded and, to associate center to star we use the rotate_points
    function to predict the center's expected position. BY comparing the expected positions with the outputs of the
    algorithm we can associate a center to each star.


    Parameters
    ----------
    Data_fits:
         :class:`pyarchi.main.initial_loads.Data` object.
    index
        image's number
    primary:
        Methodology to apply to the central star. If it's dynam then the central star is tracked using this method
    secondary:
        Methodology to apply to the outer stars. If it's dynam then they are tracked using this method

    Returns
    -------

    """

    if primary != "dynam" and secondary != "dynam":
        return

    to_calculate = []
    if primary == "dynam":
        to_calculate.append(0)

    if secondary == "dynam":
        to_calculate = to_calculate + [star.number for star in Data_fits.stars[1:]]

    scaling_factor = Data_fits.bg_grid / 200 if Data_fits.bg_grid != 0 else 1
    if index + 1 < len(Data_fits.roll_ang):

        predictions = create_predictions(Data_fits, index)
        im = Data_fits.get_image(
            index + 1
        )  # prepares the next frame for the detection routine

        _, centers, _ = shape_analysis(im, Data_fits.bg_grid, repeat_removal)

        for detected_center in centers:
            for key, pred_position in predictions.items():
                # calculate x,y coordinate of center
                if np.isclose(
                    detected_center[0], pred_position[0], atol=15 * scaling_factor
                ) and np.isclose(
                    detected_center[1], pred_position[1], atol=15 * scaling_factor
                ):
                    del predictions[key]
                    if Data_fits.stars[key].number not in to_calculate:
                        break

                    Data_fits.stars[key].add_center(detected_center)
                    break
    return 0
