import numpy as np
from scipy import optimize
from pylab import ravel
from pylab import indices
from PSF2FWHM import PSF2FWHM

import warnings
warnings.simplefilter("ignore")

##################################################################
####search max element in 2d array
def get_max(ROI):
    i,j = np.unravel_index(ROI.argmax(), ROI.shape) #get maximum pixel
    return (j, i)

##################################################################
##calculate center of mass
def centroid(R1, R2, R3, arr):
    total=0
    Ry=arr.shape[0]/2
    Rx=arr.shape[1]/2
    
    #mask
    X_index = np.arange(0, arr.shape[1], 1) ##index array
    Y_index = np.arange(0, arr.shape[0], 1) ##index array
    distance = np.sqrt(np.power(np.ones(arr.shape)*(X_index[None, :]-Rx), 2) + np.power(np.ones(arr.shape)*(Y_index[:, None]-Ry), 2)) ##distance array

    ##mean sky
    annulus_mask = np.copy(distance)
    annulus_mask[annulus_mask < R2]=0
    annulus_mask[annulus_mask > R3]=0
    annulus_mask[annulus_mask > 0 ]=1
    masked = arr*annulus_mask
    MSky=np.median(masked[np.nonzero(masked)])

    ##centroid
    aperture_mask = np.copy(distance)
    distance[distance <= R1]=1
    distance[distance > R1] =0
    masked = arr*distance
    total=np.sum(masked)
    
    X = np.sum(masked*X_index[None, :])/total
    Y = np.sum(masked*Y_index[:, None])/total
    return X-arr.shape[1]/2, Y-arr.shape[0]/2, MSky

##################################################################
##D2 moffat fitter
def D2_moffat_full(A, B, C, D, E, F, x0, y0): #B=1/sigma_x^2, C=1/sigma_y^2, E=betta
    try:
        return lambda y,x:A*(1 + ((x-x0)*B)**2+((y-y0)*C)**2+((x-x0)*(y-y0)*(D**2)))**(-E)+F
    except:
        return (None)
##read for correction of invalid value encountered in power
##http://stackoverflow.com/questions/16990664/scipy-minimize-uses-a-nonetype

def D2_moffat_fitter(ROI, MSKY, x_coo, y_coo, R3):
    x0=x_coo - np.floor(x_coo)+R3
    y0=y_coo - np.floor(y_coo)+R3
    params = (ROI.max(), 0.7, 0.7, 0.1, 5.0, np.median(ROI), x0, y0)

    errorfunction = lambda p: ravel(D2_moffat_full(*p)(*indices(ROI.shape)) - ROI)
    p, success = optimize.leastsq(errorfunction, params, maxfev=1000, ftol=0.05)
    ## print(p)

    return (p[1], p[2], p[3], p[4], p[5]), p[6]-ROI.shape[1]/2, p[7]-ROI.shape[0]/2

    
##################################################################
####
def get_PSF(Data,x_coo,y_coo):
    FWHM = 3
    R1 = int(FWHM)   ##estimation of aperture radii
    R2 = int(FWHM*6) ##sky annulus inner radii
    R3 = int(FWHM*10) ##sky annulus outer radii

##    ROI =  np.copy(Data[y_coo-R3:y_coo+R3, x_coo-R3:x_coo+R3])  #copy small area
##    offset = centroid (R1, R2, R3, ROI)                         #search centroid, Gauss sigma and mean sky

    if 1:        
##    if offset!=None:
##        x_coo = x_coo+offset[0]
##        y_coo = y_coo+offset[1]
####        print(x_coo, y_coo)
        MSKY = 0
        if R3<x_coo<(Data.shape[1]-R3) and R3<y_coo<(Data.shape[0]-R3):
            ROI =  np.copy(Data[int(round(y_coo,0))-R3:int(round(y_coo,0))+R3, int(round(x_coo,0))-R3:int(round(x_coo,0))+R3])
            param, x_fit, y_fit = D2_moffat_fitter (ROI, MSKY, x_coo, y_coo, R3)  #fit 2D moffat psf
            y_fit = int(round(y_coo,0))+y_fit
            x_fit = int(round(x_coo,0))+x_fit
            if param!=None:
                FWHM_x, FWHM_y = PSF2FWHM(param)
##                print(FWHM_x, FWHM_y)
                return(FWHM_x, FWHM_y, x_coo, y_coo, x_fit, y_fit)
        else:
            pass
##                    print('Star #', ii, ' is close to edge of frame')
    else:
        pass
##                print('Can not found centroid for star#', ii)

    return



    
