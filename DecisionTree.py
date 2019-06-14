"""
决策树分类

每个内部结点表示在一个属性上的测试，每个分支代表该测试的一个输出，每个树叶结点存放一个类标号
ID3基于信息增益作为属性选择的度量
C4.5基于信息增益比作为属性选择的度量
CART基于基尼指数作为属性选择的度量。

目标：决策树的学习，就是根据数据集构建出一棵决策树。我们希望构建出来的决策树，既能很好的对数据集进行分类，又具有很好的泛化能力。

启发式学习：由于基于特征空间划分的类的条件概率模型有无限多个，从所有可能的决策树中选取最优化决策树是NP完全问题，所以现实中决策
     树学习算法是采用启发式方法，近似求解这一最优化问题，这样得到的决策树是次优的。也就是说现实中的决策树学习算法，一般是逐步
     构建决策树，每次选取的特征是保证最优划分的，但是这样的得到的决策树不一定是所有可能的决策树中最优的。

学习过程：决策树学习算法通常就是递归的选择最优特征，并且人根据该特征对训练集进行划分，在划分之后的训练集上再进行决策树学习算法，
     如果能够大致分类，则设置成叶节点，否则继续选择最优特征，知道所有的训练数据子集都能被正确的分类或者没有可选的特征为止。

剪枝：这样的算法生成的决策树，一般对训练集的分类效果很好、但泛化能力不强，也就是说容易产生过拟合现象。因此需要对构建好的数据集
     进行剪枝，将树变得更简单，因而具有更好的泛化能力。

决策树的学习算法一般包含三个过程：特征选择、决策树生成和决策树剪枝。
"""


def InfoEntropy(xDataSet):
    """
    根据训练数据集计算香农信息熵，每个训练数据集的最后一个数据为标签信息

    :param xDataSet:训练数据集
    :return:
    """
    # 对每个标签进行统计
    labelSet = {}
    for xdata in xDataSet:
        currLabel = xdata[-1]
        if currLabel not in labelSet.keys():
            labelSet[currLabel] = 0
        labelSet[currLabel] += 1
    # 公式计算
    infoEntropy = 0.0
    numData = len(xDataSet)
    for key in labelSet:
        prob = float(labelSet[key]) / numData
        infoEntropy -= prob * log(prob, 2)
    return infoEntropy


def subDataSet(xDataSet, axis, xValue):
    """
    计算数据子集，按照属性值的取值进行计算
    返回的子集需要剔除划分的属性值，即xData[axis]

    :param xDataSet:
    :param axis:
    :param xValue:
    :return:
    """
    resultDataSet = []
    for xData in xDataSet:
        if xData[axis] == xValue:
            tempData = xData[:axis]
            tempData.extend(xData[axis + 1:])
            resultDataSet.append(tempData)
    return resultDataSet


def bestSplitFeature(xDataSet):
    """
    选择最佳的分裂属性，按照信息熵确定，取信息熵最高的类标号index

    :param xDataSet:
    :return:
    """
    # 特征数量，去掉最后一列的类标号
    numFeatures = len(xDataSet[0]) - 1
    baseInfo = InfoEntropy(xDataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        # 获取dataSet的第i个特征的所有取值
        featList = [x[i] for x in xDataSet]
        # 剔除重复取值
        uniqueVals = set(featList)
        # 经验条件熵
        newEntropy = 0.0
        # 计算信息增益
        for value in uniqueVals:
            tempDataSet = subDataSet(xDataSet, i, value)
            prob = len(tempDataSet) / float(len(xDataSet))
            newEntropy += prob * InfoEntropy(tempDataSet)
        infoGain = baseInfo - newEntropy
        # 打印每个特征的信息增益
        print("第%d个特征的增益为%.3f" % (i, infoGain))
        # 计算信息增益
        if infoGain > bestInfoGain:
            # 更新信息增益，找到最大的信息增益
            bestInfoGain = infoGain
            # 记录信息增益最大的特征的索引值
            bestFeature = i
    print('******************************')
    return bestFeature


def majorClass(xClassList):
    """
    计算xClassList中出现次数最多的类标签

    :param xClassList: 类标签集合
    :return: 出现次多的类标签
    """
    xClassCount = {}
    # 统计xClassList中每个元素出现的次数
    for vote in xClassList:
        if vote not in xClassCount.keys():
            xClassCount[vote] = 0
        xClassCount[vote] += 1
        # 根据字典的值降序排列
        sortedClassCount = sorted(xClassCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]


def createTree(xDataSet, xLabels, xFeatLabels):
    """
    创建决策树

    :param xDataSet:
    :param xLabels:
    :param xFeatLabels:
    :return:
    """
    # 取分类标签（是否放贷：yes or no）
    classList = [x[-1] for x in xDataSet]
    # 如果类别完全相同，则停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 遍历完所有特征时返回出现次数最多的类标签
    if len(dataSet[0]) == 1:
        return majorClass(classList)
    # 选择最优特征
    bestIndex = bestSplitFeature(xDataSet)
    bestFeatLabel = xLabels[bestIndex]
    featLabels.append(bestFeatLabel)
    # 根据最优特征的标签生成树
    DectionTree = {bestFeatLabel: {}}
    # 删除已经使用的特征标签
    del (xLabels[bestIndex])
    # 得到训练集中所有最优特征的属性值
    featValues = [x[bestIndex] for x in xDataSet]
    # 去掉重复的属性值
    uniqueVls = set(featValues)
    # 遍历特征，创建决策树
    for value in uniqueVls:
        tempDataSet = subDataSet(xDataSet, bestIndex, value)
        DectionTree[bestFeatLabel][value] = createTree(tempDataSet, xLabels, xFeatLabels)
    return DectionTree


def createTestData():
    # 分类属性
    xTestTrainLabel = ['年龄', '有工作', '有自己的房子', '信贷情况']
    # 数据集
    xTestDateSet = [
        [0, 0, 0, 0, 'no'],  # 01
        [0, 0, 0, 1, 'no'],  # 02
        [0, 1, 0, 1, 'yes'],  # 03
        [0, 1, 1, 0, 'yes'],  # 04
        [0, 0, 0, 0, 'no'],  # 05
        [1, 0, 0, 0, 'no'],  # 06
        [1, 0, 0, 1, 'no'],  # 07
        [1, 1, 1, 1, 'yes'],  # 08
        [1, 0, 1, 2, 'yes'],  # 09
        [1, 0, 1, 2, 'yes'],  # 10
        [2, 0, 1, 2, 'yes'],  # 11
        [2, 0, 1, 1, 'yes'],  # 12
        [2, 1, 0, 1, 'yes'],  # 13
        [2, 1, 0, 2, 'yes'],  # 14
        [2, 0, 0, 0, 'no'],  # 15
    ]
    return xTestDateSet, xTestTrainLabel


if __name__ == '__main__':
    from math import log
    import operator

    dataSet, labels = createTestData()
    featLabels = []
    myTree = createTree(dataSet, labels, featLabels)
    print(myTree)
