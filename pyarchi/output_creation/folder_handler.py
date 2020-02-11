import os


def handle_folders(number_stars, job_number, singular=None, **kwargs):
    """
        If the folder structure is not present, then it is created. If we only wish to output data for a singular star, then no more folder are created.

    Parameters
    ----------
    number_stars:
        number of stars that will have a folder
    job_number:
            Job number, from the supernova server. Will be used to save the parent folder inside the
            kwargs["results_folder"] to create the entire directory structure.
    singular:
        If it's not None, then it should be a number. Only has an effect over the graphs but, on the files, the
        light curves are all saved.
    kwargs

    Returns
    -------

    """

    path = os.path.join(kwargs["results_folder"], "{}".format(job_number))

    if not os.path.exists(path):
        os.mkdir(path)

    for j in range(number_stars):

        if singular is not None and j != singular:
            continue

        dir_name = "Star_{}".format(j)

        star_path = os.path.join(path, dir_name)
        if not os.path.exists(star_path):
            os.mkdir(star_path)

    return path


if __name__ == "__main__":
    handle_folders(2, 1, **{"results_folder": "."})
