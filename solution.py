from scipy.stats import anderson_ksamp
import pandas as pd
import numpy as np

chat_id = 704471350

def solution(x: np.array, y: np.array) -> bool:
    Anderson_test = anderson_ksamp([x,y])
    alpha = 0.1
    if alpha < Anderson_test.pvalue:
      res = False
    else:
      res = True
    return res
