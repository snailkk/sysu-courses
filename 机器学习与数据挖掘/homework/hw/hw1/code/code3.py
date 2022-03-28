import numpy as np
import pandas as pd
import math

def func(x,y):
    tmp1 = y**2*math.exp(-(y**2))
    tmp2 = x**4*math.exp(-(x**2))
    tmp3 = x*math.exp(-(x**2))
    return (tmp1 + tmp2) / tmp3

def mento_carlo(sample_num,area):
    ret = [str(sample_num),0.0,0.0]

    result = [0.0] * 100
    for i in range(100):
        samples_x = np.random.uniform(2,4,[1,sample_num])
        samples_y = np.random.uniform(-1,1,[1,sample_num])
        for j in range(len(samples_x[0])):
            result[i] += func(samples_x[0][j],samples_y[0][j])

        result[i] *= (area/sample_num)

    result_ = np.array(result)
    ret[1]  = result_.mean()
    ret[2]  = result_.var()
    return ret

if __name__ == "__main__":
    sample_numList = [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500]
    ret = []
    for sample_num in sample_numList:
        ret.append(mento_carlo(sample_num,4.0))
    df = pd.DataFrame(ret, columns = ['sample_num','mean','variance'])
    print(df)
