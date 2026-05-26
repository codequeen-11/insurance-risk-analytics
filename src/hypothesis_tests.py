from scipy.stats import ttest_ind, chi2_contingency
import pandas as pd

def chi_square_test(data, col1, col2):
    table = pd.crosstab(data[col1], data[col2])
    chi2, p, dof, expected = chi2_contingency(table)
    return p

def t_test(group1, group2):
    stat, p = ttest_ind(group1, group2, equal_var=False)
    return p