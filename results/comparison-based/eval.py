from scipy import stats
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.metrics import mean_squared_error
from math import sqrt

from numpy.polynomial.polynomial import polyfit
import seaborn as sns

import numpy as np
import pandas as pd

def pearsonr_ci(x,y,alpha=0.05):
    ''' calculate Pearson correlation along with the confidence interval using scipy and numpy
    Parameters
    ----------
    x, y : iterable object such as a list or np.array
      Input for correlation calculation
    alpha : float
      Significance level. 0.05 by default
    Returns
    -------
    r : float
      Pearson's correlation coefficient
    pval : float
      The corresponding p value
    lo, hi : float
      The lower and upper bound of confidence intervals
    '''
    N = len(x)
    r, p = stats.pearsonr(x,y)
    r_z = np.arctanh(r)
    se = 1/np.sqrt(N-3)
    z = stats.norm.ppf(1-alpha/2)
    lo_z, hi_z = r_z-z*se, r_z+z*se
    lo, hi = np.tanh((lo_z, hi_z))
    return r, p, lo, hi


df = pd.read_csv('predictions.csv', sep=',', header=0)
gt_scores = df.loc[:, 'gt_scores']
pred = df.loc[:, 'predictions']

print('* Results *')
corr, p, lo, hi = pearsonr_ci(gt_scores, pred)
print('PCC: r=%.2f, p=%.2e, CI=[%.2f, %.2f]' % (corr, p, lo, hi))
rmse_test = sqrt(mean_squared_error(gt_scores, pred))
print('RMSE: %.3f' % rmse_test)