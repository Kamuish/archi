import numpy as np


def DRP_CDPP(photom, jd, twidth):
    """
    Compute the Combined Differential Photometric Precision (CDPP) metric.
    This definition estimates the unbiased variance of a rolling window of size twidth
    (in sample units) and returns the sqrt( meadian (var) ) / sqrt (norm) where norm
    is the average number of points in the windows.
    This implementation is robust against gaps in the light curve.

    @author Sergio Hoyer, Pascal Guterman

    Parameters
    ------------------
        flux : Flux. 1d ndarray time series.
        jd : Timescale (in days). 1d ndarray of same size.
        twidth: temporal width where the CDPP is estimated (same units as JD)


    Returns
    --------------
        CDPP: SQRT ( MEDIAN ( VAR_ARRAY ) ) / SQRT(NORM)
        WINDOW_SIZE: CONSTANT. Number of points in rolling windows


    Syntax
    ---------
        cdpp, wsize = cdpp(flux, jd, twidth)

    Example
    -------------
    """
    if photom == []:
        print("No values provided for CDPP")
        return float("nan")

    flux = 1e6 * (photom / np.mean(photom) - 1)  # normalized flux on ppm

    # Convert to sample numbers
    texp = np.median(np.diff(jd))  # Exposure time
    nexp = len(flux)  # Number of points in the LC
    # Evenly spaced signal
    index = np.round((jd - np.min(jd)) / texp).astype(int)
    eflux = np.ones(1 + np.max(index)) * np.nan

    try:
        eflux[index] = flux
    except Exception as e:
        print(jd)
        print(type(photom))
        print(photom)
        print(index)
        print(eflux)
        raise (e)

    xwidth = np.round(twidth / texp).astype(int)  # Requested time width (in sample unit)
    wsize = np.clip(
        xwidth, 2, nexp
    )  # Sliding window, minimum length 2 points / max full curve

    # To mute the warning rise by numpy nanvar when the rolling window is full of nans (gaps)
    with np.warnings.catch_warnings():
        np.warnings.filterwarnings("ignore", category=RuntimeWarning)

        # array with the variance on each rolling window using unbiased estimator (N-1)
        vararr = [
            np.nanvar(eflux[i : i + wsize], ddof=1) for i in range(nexp - wsize + 1)
        ]

    # Convention length param = 0 returns point to point noise

    # Normalization factor of the standard deviation
    norm = np.clip(xwidth, 1, nexp)

    return np.sqrt(np.nanmean(vararr)) / np.sqrt(norm)


if __name__ == "__main__":
    pass
