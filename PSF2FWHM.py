import numpy as np


def PSF2FWHM(PSF_model):
    try:
        phi = np.arctan((PSF_model[2] ** 2) / (PSF_model[0] ** 2 - PSF_model[1] ** 2)) / 2
        alpha1 = np.sqrt(2 / (PSF_model[0] ** 2 + PSF_model[1] ** 2 + PSF_model[2] ** 2 / np.sin(2 * phi)))
        alpha2 = np.sqrt(np.fabs(1 / (PSF_model[0] ** 2 + PSF_model[1] ** 2 - 1 / (alpha1 ** 2))))
        FWHM1 = 2 * alpha1 * np.sqrt(2 ** (1 / (PSF_model[3])) - 1)
        FWHM2 = 2 * alpha2 * np.sqrt(2 ** (1 / (PSF_model[3])) - 1)
        return (FWHM1, FWHM2)

    except:
        print('Wrong PSF model')
        return (0, 0)