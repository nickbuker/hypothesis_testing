import scipy.stats


def p_value(z_score, tails=2):
    """
    Input: z score and tails (1 for one-tailed, 2 for two- tailed)
    Output: p value
    """
    return scipy.stats.norm.sf(abs(z_score)) * tails
