import numpy as np
import pandas as pd

def is_in(coordinate):
    distance = coordinate[0] ** 2 + coordinate[1] ** 2
    distance = distance ** 0.5
    if distance < 1:
        return True
    else:
        return False

def mento_carlo(sample_num):
    ret = [str(sample_num),0.0,0.0]

    result = [0.0] * 100
    for i in range(100):
        samples = np.random.rand(sample_num,2)

        for sample in samples:
            if is_in(sample):
                result[i] += 1

        result[i] /= sample_num
        result[i] *= 4
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
