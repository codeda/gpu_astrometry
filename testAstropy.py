


from astropy.stats import sigma_clipped_stats
from photutils import datasets
hdu = datasets.load_star_image()
w=1059
h=1059
data = hdu.data[0:w, 0:h]
mean, median, std = sigma_clipped_stats(data, sigma=3.0, iters=5)
print((mean, median, std))

from photutils import IRAFStarFinder
daofind = IRAFStarFinder(fwhm=3.0, threshold=5.*std)
sources = daofind(data - median)
#print(sources)

import matplotlib.pyplot as plt
import getpsf
for i in range(len(sources)):
    sx=sources[i]['xcentroid']
    sy=sources[i]['ycentroid']
    psf = getpsf.get_PSF(data, sx, sy)
    if psf is not None:
        FWHM_x, FWHM_y, x_coo, y_coo, x_fit, y_fit = psf
        data[int(round(y_fit,0))][int(round(x_fit))] = 0

plt.imsave('/home/ubuntu/test_astropy.png',data, cmap='Greys', origin='lower')



