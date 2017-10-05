


from astropy.stats import sigma_clipped_stats
from photutils import datasets
hdu = datasets.load_star_image()

data = hdu.data[0:1059, 0:1059]
mean, median, std = sigma_clipped_stats(data, sigma=3.0, iters=5)
print((mean, median, std))

from photutils import IRAFStarFinder
daofind = IRAFStarFinder(fwhm=3.0, threshold=5.*std)
sources = daofind(data - median)
#print(sources)

import matplotlib.pyplot as plt
from astropy.visualization import SqrtStretch
from astropy.visualization.mpl_normalize import ImageNormalize
from photutils import CircularAperture
m = [[0 for x in range(1059)] for y in range(1059)]

for i in range(1269):
    sx=int(sources[i]['xcentroid'])
    sy=int(sources[i]['ycentroid'])
    data[sy][sx] = 0
plt.imsave('/home/ubuntu/test_astropy.png',data, cmap='Greys', origin='lower')



