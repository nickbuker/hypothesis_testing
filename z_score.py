from __future__ import division
import numpy as np


def z_score(A, B, test_type):
    """
    Input: numpy arrays for A and B and test_type 'prop' or 'mean'
    Output: z score
    """
    XA, XB = sum(A), sum(B)
    NA, NB = len(A), len(B)
    if test_type == 'prop':
        p_pool = (XA + XB) / (NA + NB)
        SE_pool = (p_pool * (1 - p_pool) * ((1 / NA) + (1 / NB))) ** 0.5
        return ((XB / NB) - (XA / NA)) / SE_pool
    if test_type == 'mean':
        mu_A, mu_B = XA / NA, XB / XA
        var_A = np.sum((A - mu_A) ** 2) / NA
        var_B = np.sum((B - mu_B) ** 2) / NB
        SE = ((var_A / NA) + (var_B / NB)) ** 0.5
        return (mu_B - mu_A) / SE
