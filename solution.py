import pandas as pd
import numpy as np
from math import sqrt

chat_id = 704471350

def solution(x: np.array, y: np.array) -> bool:
    m = len(x)
    n = len(y)
    x_avr = sum(x)/m
    y_avr = sum(y)/n

    s_t1 = 0
    S_x = 0
    for i in range(m):
      s_t1 = (x[i] - x_avr)**2
      S_x +=s_t1

    s_t2 = 0
    S_y = 0
    for i in range(n):
      s_t2 = (y[i] - y_avr)**2
      S_y +=s_t2

    s2_x = S_x/(m-1)
    s2_y = S_y/(n-1)

    t = ((x_avr-y_avr)/(sqrt((m-1)*s2_x + (n-1)*s2_y))) * sqrt( (m*n*(m+n-2))/(m+n) )

    t_crit = 2.33
    if t < t_crit:
      res = False
    else:
      res = True

    return res
