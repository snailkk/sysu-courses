import numpy as np
import pandas as pd

def mento_carlo(sample_num):
    ret = [str(sample_num),0.0,0.0]

    result = [0.0] * 100
    for i in range(100):
        samples = np.random.rand(sample_num,3)

        for sample in samples:
            p_A = sample[0]
            p_B = sample[1]
            p_C = sample[2]

            if p_A <= 0.85:
                result[i] += 1
            elif p_B <= 0.95 and p_C <= 0.90:
                result[i] += 1

        result[i] /= sample_num
    result_ = np.array(result)
    ret[1]  = result_.mean()
    ret[2]  = result_.var()

    return ret

if __name__ == "__main__":
    sample_numList = [20,50,100,200,300,500,1000,5000]
    ret = []
    for sample_num in sample_numList:
        ret.append(mento_carlo(sample_num))
    df = pd.DataFrame(ret, columns = ['sample_num','mean','variance'])
    print(df)
