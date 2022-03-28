import numpy as np
import pandas as pd

def func(x):
    return pow(x,3)

def mento_carlo(sample_num,area):
    ret = [str(sample_num),0.0,0.0]

    result = [0.0] * 100
    for i in range(100):
        samples = np.random.uniform(0,1,[1,sample_num])

        for sample in samples[0]:
            result[i] += func(sample)

        result[i] *= (area/sample_num)

    result_ = np.array(result)
    ret[1]  = result_.mean()
    ret[2]  = result_.var()
    return ret

if __name__ == "__main__":
    sample_numList = [5, 10, 20, 30, 40, 50, 60, 70, 80, 100]
    ret = []
    for sample_num in sample_numList:
        ret.append(mento_carlo(sample_num,1.0))
    df = pd.DataFrame(ret, columns = ['sample_num','mean','variance'])
    print(df)
