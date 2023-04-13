import scipy.stats as stats
import pandas as pd
import numpy as np

chat_id = 704471350

def solution(x: np.array, y: np.array) -> bool:
    Ttest = stats.ttest_ind(a=x, b=y, equal_var=False)
    alpha = 0.1
    print(Ttest.pvalue)
    print(alpha)
    if alpha < Ttest.pvalue:
      res = False
    else:
      res = True
    return res
