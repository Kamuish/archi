import numpy as np
from scipy.signal import savgol_filter
from ARCHI.utils import create_logger

logger = create_logger("utils")


def Chunks(l, n, all=False):
    if all:
        jarr = range(0, n - 1)
    else:
        jarr = [0]

    for j in jarr:
        for i in range(j, len(l), n):
            if i + 2 * n <= len(l):
                yield l[i : i + n]
            else:
                if not all:
                    yield l[i:]
                break


def CDPP(flux_vals, sized=41, winlen=10, win=30, outl=True):
    """

    Parameters
    ----------
    flux_vals:
        flux values
    sized:
        Since we are calculating the CDPP for 1 hour. Window for the Savgol filter
    winlen:
        Convolution window
    win
        Time over which we want to calculate the CDPP

    outl:
        Remove the outliers.

    Returns
    -------

    """
    if flux_vals == []:
        logger.fatal("No values provided")
        return float("nan")

    planeta2 = SavGol(flux_vals, win=sized)

    planeta2 = planeta2 / np.nanmedian(planeta2)

    s = np.r_[
        2 * planeta2[0] - planeta2[winlen - 1 :: -1],
        planeta2,
        2 * planeta2[-1] - planeta2[-1:-winlen:-1],
    ]
    w = np.hanning(winlen)
    planeta3 = np.convolve(w / w.sum(), s, mode="same")
    planeta3 = planeta3[winlen : -winlen + 1]

    planeta4 = planeta2 - planeta3

    M = np.nanmedian(planeta4)
    MAD = 1.4826 * np.nanmedian(np.abs(planeta4 - M))
    out = []
    for i, _ in enumerate(planeta4):
        if (planeta4[i] > M + 5 * MAD) or (planeta4[i] < M - 5 * MAD):
            out.append(i)
    if outl:
        out = np.array(out, dtype=int)
        planeta2 = np.delete(planeta2, out)

    cdpp = 1.0e6 * np.nanmedian(
        [np.std(yi) / np.sqrt(win) for yi in Chunks(planeta2, win, all=False)]
    )  # *1.168
    return cdpp


def Interpolate(time, mask, y):
    """
    Masks certain elements in the array `y` and linearly
    interpolates over them, returning an array `y'` of the
    same length.

    :param array_like time: The time array
    :param array_like mask: The indices to be interpolated over
    :param array_like y: The dependent array

    """

    # Ensure `y` doesn't get modified in place
    yy = np.array(y)
    t_ = np.delete(time, mask)
    y_ = np.delete(y, mask, axis=0)
    if len(yy.shape) == 1:
        yy[mask] = np.interp(time[mask], t_, y_)
    elif len(yy.shape) == 2:
        for n in range(yy.shape[1]):
            yy[mask, n] = np.interp(time[mask], t_, y_[:, n])
    else:
        raise Exception("Array ``y`` must be either 1- or 2-d.")
    return yy


def Scatter(y, win=13, remove_outliers=False):
    """
    Return the scatter in ppm based on the median running standard deviation
    for a window size of :py:obj:`win` = 13 cadences (for K2, this
    is ~6.5 hours, as in VJ14).

    :param ndarray y: The array whose CDPP is to be computed
    :param int win: The window size in cadences. Default `13`
    :param bool remove_outliers: Clip outliers at 5 sigma before computing \
           the CDPP? Default `False`

    """

    if remove_outliers:
        # Remove 5-sigma outliers from data
        # smoothed on a 1 day timescale
        if len(y) >= 50:
            ys = y - Smooth(y, 50)
        else:
            ys = y
        M = np.nanmedian(ys)
        MAD = 1.4826 * np.nanmedian(np.abs(ys - M))
        out = []
        for i, _ in enumerate(y):
            if (ys[i] > M + 5 * MAD) or (ys[i] < M - 5 * MAD):
                out.append(i)
        out = np.array(out, dtype=int)
        y = np.delete(y, out)
    if len(y):
        return 1.0e6 * np.nanmedian(
            [np.std(yi) / np.sqrt(win) for yi in Chunks(y, win, all=True)]
        )
    else:
        return np.nan


def Smooth(x, window_len=100, window="hanning"):
    """
    Smooth data by convolving on a given timescale.

    :param ndarray x: The data array
    :param int window_len: The size of the smoothing window. Default `100`
    :param str window: The window type. Default `hanning`


    """

    if window_len == 0:
        return np.zeros_like(x)
    s = np.r_[2 * x[0] - x[window_len - 1 :: -1], x, 2 * x[-1] - x[-1:-window_len:-1]]
    if window == "flat":
        w = np.ones(window_len, "d")
    else:
        w = eval("np." + window + "(window_len)")
    y = np.convolve(w / w.sum(), s, mode="same")
    return y[window_len : -window_len + 1]


def SavGol(y, win=49):
    """
    Subtracts a second order Savitsky-Golay filter with window size `win`
    and returns the result. This acts as a high pass filter.

    """

    if len(y) >= win:
        return y - savgol_filter(y, win, 2) + np.nanmedian(y)
    else:
        return y
