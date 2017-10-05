


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
for i in range(len(sources)):
    sx=int(sources[i]['xcentroid'])
    sy=int(sources[i]['ycentroid'])
    data[sy][sx] = 0
plt.imsave('/home/ubuntu/test_astropy.png',data, cmap='Greys', origin='lower')



