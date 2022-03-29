import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random
import math
import copy


def getData(filename):
    '''读取数据

    Args:
      filename 文件名（包含路径）

    Returns:
      data
    '''
    np.set_printoptions(suppress=True)

    file = open(filename)
    lines = file.readlines()
    lineNum = len(lines)

    data = np.zeros((lineNum, 7), dtype=np.longdouble)
    index = 0

    for line in lines:
        line = line.strip()
        lineData = line.split(' ')
        data[index, :] = lineData[0: 7]
        index += 1

    return data


def sigmod(z):
    '''逻辑函数

    Args:
        z

    Returns:
        1/(1 + e^{-z})
    '''
    return ((np.exp(z) / (np.longdouble(1.0) + np.exp(z))))


def gradientDecent(learning_rate=0.00015, theta = np.zeros((7, 1), dtype=np.longdouble), iteration_time=1500000, show_margin=100000, random_points=0):
    '''梯度下降训练线性模型

    Args:
        learning_rate: 学习率
        iteration_time: 迭代次数
        show_margin: 数据展示的迭代次数间隔
        theta: 7个参数

    Returns:
        iterationTimes: 迭代次数数组
        targetFunc_List_train: 训练误差
        targetFunc_List_test: 测试误差
        resTable: 结果表
    '''
    # 获取数据
    # print(theta)
    trainSet = getData('../data/dataForTrainingLogistic.txt')  # 训练集
    testSet = getData('../data/dataForTestingLogistic.txt')  # 测试集
    trainSetSize = len(trainSet)  # 训练集大小
    testSetSize = len(testSet)  # 测试集大小

    resTable = PrettyTable(["iteration_times", "theta_0", "theta_1","theta_2", "theta_3","theta_4", "theta_5","theta_6"])
                            # "theta_6", "training_TargetFunc", "testing_TargetFunc"])
    targetFunc_List_train = []  # 训练误差
    targetFunc_List_test = []  # 测试误差
    iterationTimes = []  # 迭代次数

   #构建训练集的自变量矩阵X_train，大小为trainSetSize*3,因变量向量Y_train,大小为trainSetSize*1
    X_train = np.ones((trainSetSize, 7), dtype=np.longdouble)
    X_train[:,1:] = trainSet[:,0:6]

    Y_train = np.ones((trainSetSize, 1), dtype=np.longdouble)
    Y_train [:,0] = trainSet[:,6]

    #如上构造测试集
    X_test = np.ones((testSetSize, 7), dtype=np.longdouble)
    X_test[:,1:] = testSet[:,0:6]

    Y_test = np.ones((testSetSize, 1), dtype=np.longdouble)
    Y_test [:,0] = testSet[:,6]

    m = 0
    if (random_points == 0):
        # 正常梯度下降迭代
        X = X_train[:,:]
        Y = Y_train[:,:]
        m = trainSetSize

    for iterTime in range(1, iteration_time + 1):

        if random_points == 0 or random_points >= trainSetSize:
            pass
        else:
            index = random.randint(random_points, trainSetSize - 1)
            # print(index)
            # 随机梯度下降迭代
            X = X_train[index - random_points:index,:]
            Y = Y_train[index - random_points:index,:]
            m = random_points

        # 更新参数
        theta = theta + (learning_rate/m)*np.dot(X.T,Y - sigmod(np.dot(X,theta)))

        if (iterTime % show_margin == 0):
            print("迭代次数: ", iterTime)
            iterationTimes.append(iterTime + 1)

            targetFunc_train = -np.dot(np.ones((trainSetSize,1)).T,(-Y_train*np.dot(X_train,theta)+(np.log(np.longdouble(1.0)+np.exp(np.dot(X_train,theta))))))/trainSetSize
            targetFunc_List_train.append(targetFunc_train[0][0])

            targetFunc_test = -np.dot(np.ones((testSetSize,1)).T,(-Y_test*np.dot(X_test,theta)+(np.log(np.longdouble(1.0)+np.exp(np.dot(X_test,theta))))))/testSetSize
            targetFunc_List_test.append(targetFunc_test[0][0])

            resTable.add_row([iterTime, theta[0][0], theta[1][0],theta[2][0],theta[3][0], theta[4][0],theta[5][0], theta[6][0]])

    return (iterationTimes, targetFunc_List_train, targetFunc_List_test, resTable)


(iterationTimes, targetFunc_List_train_0, targetFunc_List_test_0,
 resTable_0) = gradientDecent(learning_rate= 0.1, iteration_time=1000000, show_margin=100000,random_points=0)#每次迭代全部样本做训练


(iterationTimes, targetFunc_List_train_1, targetFunc_List_test_1,
 resTable_1) = gradientDecent(learning_rate= 0.1, iteration_time=1000000, show_margin=100000,random_points=1)#每次迭代随机一个样本做训练

#打出参数表
# print(resTable)

# 画图
plt.figure()
plt.plot(iterationTimes, targetFunc_List_test_0, "+-",
         c="r", linewidth=1, label="$TargetFunc_{test}$")
plt.plot(iterationTimes, targetFunc_List_train_0, "X-",
         c="b", linewidth=1, label="$TargetFunc_{train}$")

plt.plot(iterationTimes, targetFunc_List_test_1, "+-",
         c="g", linewidth=1, label="$TargetFunc1_{test}$")
plt.plot(iterationTimes, targetFunc_List_train_1, "X-",
         c="y", linewidth=1, label="$TargetFunc1_{train}$")

plt.xlabel("Iteration Times")
plt.ylabel("TargetFunc")
plt.legend()
# plt.title("Gradient Descent")
plt.show()
