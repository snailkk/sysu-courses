import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import random


def getData(filename):
    np.set_printoptions(suppress=True)

    file = open(filename)
    lines = file.readlines()
    lineNum = len(lines)

    data = np.zeros((lineNum, 3), dtype=np.float64)
    index = 0

    for line in lines:
        line = line.strip()
        lineData = line.split(' ')
        data[index, :] = lineData[0: 3]
        index += 1

    return data

# testSet = getData('../data/dataForTestingLinear.txt')
# print(testSet)
def gradientDecent(learning_rate=0.00015, theta = np.zeros((3, 1), dtype=np.float64), iteration_time=1500000, show_margin=100000, random_points=0):
    '''梯度下降训练线性模型

    Args:
        learning_rate: 学习率
        theta:模型参数,初始参数为3*1的全0向量
        iteration_time: 迭代次数
        show_margin: 数据展示的迭代次数间隔

    Returns:
        iterationTimes: 迭代次数数组
        trainingErrors: 训练误差
        testingErrors: 测试误差
        resTable: 结果表
    '''
    # 获取数据
    trainSet = getData('../data/dataForTrainingLinear.txt')  # 训练集
    testSet = getData('../data/dataForTestingLinear.txt')  # 测试集
    trainSetSize = len(trainSet)  # 训练集大小
    testSetSize = len(testSet)  # 测试集大小

    #构建训练集的自变量矩阵X_train，大小为trainSetSize*3,因变量向量Y_train,大小为trainSetSize*1
    X_train = np.ones((trainSetSize, 3), dtype=np.float64)
    X_train[:,1:] = trainSet[:,0:2]

    Y_train = np.ones((trainSetSize, 1), dtype=np.float64)
    Y_train [:,0] = trainSet[:,2]

    #如上构造测试集
    X_test = np.ones((testSetSize, 3), dtype=np.float64)
    X_test[:,1:] = testSet[:,0:2]

    Y_test = np.ones((testSetSize, 1), dtype=np.float64)
    Y_test [:,0] = testSet[:,2]

    # print(Y_train)
    # print(Y_test)

    resTable = PrettyTable(["iteration_times", "theta_0", "theta_1",
                            "theta_2", "training_error", "testing_error"])
    trainingErrors = []  # 训练误差
    testingErrors = []  # 测试误差
    iterationTimes = []  # 迭代次数


    m = 0
    if (random_points == 0):
        # 正常梯度下降迭代
        X = X_train[:,:]
        Y = Y_train[:,:]
        m = trainSetSize

    for iterTime in range(1, iteration_time + 1):
        if (random_points != 0):
            index = random.randint(random_points, trainSetSize - 1)
            # 随机梯度下降迭代
            X = X_train[index - random_points:index,:]
            Y = Y_train[index - random_points:index,:]
            m = random_points

        # 迭代参数
        theta = theta - (learning_rate/m)*(np.dot(X.T,np.dot(X,theta) - Y))

        # 每间隔 show_margin 次进行一次结果展示
        if (iterTime % show_margin == 0):
            print("迭代次数: ", iterTime)
            iterationTimes.append(iterTime + 1)

            trainError = np.dot((Y_train - np.dot(X_train,theta)).T,
                                    (Y_train - np.dot(X_train,theta)))/(2*trainSetSize)
            trainingErrors.append(trainError[0][0])

            testError = np.dot((Y_test - np.dot(X_test,theta)).T   ,
                                (Y_test - np.dot(X_test,theta)))/(2*testSetSize)
            testingErrors.append(testError[0][0])

            resTable.add_row([iterTime, theta[0][0], theta[1][0],theta[2][0], trainError[0][0], testError[0][0]])

    return (iterationTimes, trainingErrors, testingErrors, resTable)


(iterationTimes, trainingErrors, testingErrors,
 resTable) = gradientDecent(learning_rate=0.00015, iteration_time=1500000, show_margin=100000, random_points=0)


print(resTable)

# 画图
plt.figure()
plt.plot(iterationTimes, trainingErrors, "+-",
         c="g", linewidth=1, label="$Error\_train_{theta}$")
plt.plot(iterationTimes, testingErrors, "X-",
         c="b", linewidth=1, label="$Error\_test_{theta}$")

plt.xlabel("Iteration Times")
plt.ylabel("Error")
plt.legend()
# plt.title("Gradient Descent")
plt.show()