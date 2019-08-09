import numpy as np
import matplotlib.pyplot as plt
import operator

def fileTomatrix(filename):
    """
    读取文本文件
    :param filename:
    :return:
    """
    with open(filename,'r') as f:
        #获取文件中数据的行数
        lines = len(f.readlines())
        #生成对应的空矩阵
        returnMat = np.zeros((lines,3))
    classLabelVector = []   #分类
    index = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            #去除这行字符后面的所有空格 用replace可以去除全部空格
            line=line.strip()
            listFromLine = line.split("\t")

            #特征值
            returnMat[index,:]=listFromLine[0:3]
            #分类情况
            classLabelVector.append(listFromLine[-1])

            index+=1
        return returnMat,classLabelVector

def autoNorm(dataSet):
    """
    归一化 消除属性之间量级不同造成的印象
    公式 Y=(X-Xmin)/(Xmax-Xmin)
    :param dataSet:
    :return:
    """
    max_value = dataSet.max()
    min_vlaue = dataSet.min()
    normDataSet = (dataSet-min_vlaue)/(max_value-min_vlaue)
    return normDataSet


if __name__=="__main__":
    res,label=fileTomatrix('data')
    normSet= autoNorm(res)

    print(normSet)