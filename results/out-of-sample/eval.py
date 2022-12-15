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


df_rb = pd.read_csv('predictions_rb.csv', sep=',', header=0)
df_cb = pd.read_csv('predictions_cb.csv', sep=',', header=0)

y_val_rb = df_rb['mean_rating']
pred_rb = df_rb['prediction']
y_val_cb = df_cb['comparison_based_score']
pred_cb = df_cb['prediction']


print('* Rating-based model *')
corr, p, lo, hi = pearsonr_ci(y_val_rb, pred_rb)
print('PCC - user ratings: r=%.2f, p=%.2e, CI=[%.2f, %.2f]' % (corr, p, lo, hi))
rmse_test = sqrt(mean_squared_error(y_val_rb, pred_rb))
print('RMSE - user ratings: %.3f' % rmse_test)

corr, p, lo, hi = pearsonr_ci(y_val_cb, pred_rb)
print('PCC - comparison-based user scores: r=%.2f, p=%.2e, CI=[%.2f, %.2f]' % (corr, p, lo, hi))
rmse_test = sqrt(mean_squared_error(y_val_cb, pred_rb))
print('RMSE - comparison-based user scores: %.3f' % rmse_test)

print('\n')

print('* Comparison-based model *')
corr, p, lo, hi = pearsonr_ci(y_val_rb, pred_cb)
print('PCC - user ratings: r=%.2f, p=%.2e, CI=[%.2f, %.2f]' % (corr, p, lo, hi))
rmse_test = sqrt(mean_squared_error(y_val_rb, pred_cb))
print('RMSE - user ratings: %.3f' % rmse_test)

corr, p, lo, hi = pearsonr_ci(y_val_cb, pred_cb)
print('PCC - comparison-based user scores: r=%.2f, p=%.2e, CI=[%.2f, %.2f]' % (corr, p, lo, hi))
rmse_test = sqrt(mean_squared_error(y_val_cb, pred_cb))
print('RMSE - comparison-based user scores: %.3f' % rmse_test)