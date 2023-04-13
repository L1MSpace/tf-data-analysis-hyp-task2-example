from scipy.stats import ks_2samp
import pandas as pd
import numpy as np

chat_id = 704471350

def solution(x: np.array, y: np.array) -> bool:
    KStest = ks_2samp(x, y)
    alpha = 0.1
    if alpha < KStest.pvalue:
      res = False
    else:
      res = True
    return res
