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

学习过程：决策树学习算法通常就是递归的选择最优特征，兵器人根据该特征对训练集进行划分，在划分之后的训练集上再进行决策树学习算法，
     如果能够大致分类，则设置成叶节点，否则继续选择最优特征，知道所有的训练数据子集都能被正确的分类或者没有可选的特征为止。

剪枝：这样的算法生成的决策树，一般对训练集的分类效果很好、但泛化能力不强，也就是说容易产生过拟合现象。因此需要对构建好的数据集
     进行剪枝，将树变得更简单，因而具有更好的泛化能力。

决策树的学习算法一般包含三个过程：特征选择、决策树生成和决策树剪枝。
"""

__author__ = 'Zeros'


class DecisonTree:
    def __init__(self, xtrainData, xtrainLabel, xthreshold):
        self._trainData = []
        self._trainLabel = []
        self._featureValus = {}
        self.loadData(xtrainData, xtrainLabel)
        self.threshold = xthreshold
        self.tree = self.createTree(range(0, len(xtrainLabel)), range(0, len(xtrainData[0])))

    # 加载数据
    def loadData(self, xtrainData, xtrainLabel):
        if len(xtrainData) != len(xtrainLabel):
            raise ValueError('input error')
        self._trainData = xtrainData
        self._trainLabel = xtrainLabel
        # 计算 featureValus
        for data in xtrainData:
            for index, value in enumerate(data):
                if index not in self._featureValus.keys():
                    self._featureValus[index] = [value]
                if value not in self._featureValus[index]:
                    self._featureValus[index].append(value)

    # 计算信息熵
    def caculateEntropy(self, dataset):
        labelCount = self.labelCount(dataset)
        size = len(dataset)
        result = 0
        for i in labelCount.values():
            pi = i / float(size)
            result -= pi * (log(pi) / log(2))
        return result

    # 计算数据集中，每个标签出现的次数
    def labelCount(self, xdataset):
        tempCount = {}
        for i in xdataset:
            if self._trainLabel[i] in tempCount.keys():
                tempCount[self._trainLabel[i]] += 1
            else:
                tempCount[self._trainLabel[i]] = 1
        return tempCount

    # 计算信息增益
    def caculateGain(self, dataset, feature):
        values = self._featureValus[feature]  # 特征feature 所有可能的取值
        result = 0
        for v in values:
            subDataset = self.splitDataset(xdataset=dataset, xfeature=feature, xvalue=v)
            result += len(subDataset) / float(len(dataset)) * self.caculateEntropy(subDataset)
        return self.caculateEntropy(dataset=dataset) - result

    def splitDataset(self, xdataset, xfeature, xvalue):
        reslut = []
        for index in xdataset:
            if self._trainData[index][xfeature] == xvalue:
                reslut.append(index)
        return reslut

    def createTree(self, dataset, features):

        labelCount = self.labelCount(dataset)
        # 如果特征集为空，则该树为单节点树
        # 计算数据集中出现次数最多的标签
        if not features:
            return max(list(labelCount.items()), key=lambda x: x[1])[0]

        # 如果数据集中，只包同一种标签，则该树为单节点树
        if len(labelCount) == 1:
            return labelCount.keys()[0]

        # 计算特征集中每个特征的信息增益
        l = map(lambda x: [x, self.caculateGain(dataset=dataset, feature=x)], features)

        # 选取信息增益最大的特征
        feature, gain = max(l, key=lambda x: x[1])

        # 如果最大信息增益小于阈值，则该树为单节点树
        if self.threshold > gain:
            return max(list(labelCount.items()), key=lambda x: x[1])[0]

        tempTree = {}
        # 选取特征子集
        subFeatures = filter(lambda x: x != feature, features)
        tree['feature'] = feature
        # 构建子树
        for value in self.featureValus[feature]:
            subDataset = self.splitDataset(dataset=dataset, feature=feature, value=value)

            # 保证子数据集非空
            if not subDataset:
                continue
            tree[value] = self.createTree(dataset=subDataset, features=subFeatures)
        return tree

    def classify(self, data):
        def f(tree, data):
            if type(tree) != dict:
                return tree
            else:
                return f(tree[data[tree['feature']]], data)

        return f(self.tree, data)


if __name__ == '__main__':
    from numpy import log

    trainData1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 1, 2],
        [1, 0, 1, 2],
        [2, 0, 1, 2],
        [2, 0, 1, 1],
        [2, 1, 0, 1],
        [2, 1, 0, 2],
        [2, 0, 0, 0],
    ]
    trainLabel1 = [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0]
    tree = DecisonTree(trainData=trainData1, trainLabel=trainLabel1, threshold=0)
    print(tree.tree)
