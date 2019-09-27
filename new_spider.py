import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

import time
# 爬虫地址
url = 'http://9x906.com/api/game/k3OpenList?lotteryid=65'
file_name="recode.txt"
# 携带cookie进行访问
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
   'Cookie': 'td_cookie=3606231329; PHPSESSID=95hjt64h922bvlk1i77afhohr1; username=libuda; nickname=%E7%AD%BE%E6%8A%95%E6%83%8A%E7%90%85; roomId=81259577540609; vocabulary=%E6%93%8D%E4%BD%A0%E5%A6%88%EF%BC%8C%E6%BB%9A%EF%BC%8C%E5%82%BB%E9%80%BC%EF%BC%8C%E4%BD%A0%E5%A6%88%E9%80%BC%EF%BC%8C%E5%9E%83%E5%9C%BE%EF%BC%8C%E5%9D%91%E4%BA%BA%EF%BC%8C%E5%9D%91%E7%88%B9%EF%BC%8C%E5%9D%91%E9%92%B1%EF%BC%8C%E5%B9%B3%E5%8F%B0%EF%BC%8C%E5%A6%88%E5%8D%96%E6%89%B9',
    'Host': '9x906.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
}
dic={}
flag1=0  #大
flag2=0  #小
flag3=0   #单
flag4=0 #双


def getAnylize(m):
    """
    获取最近m期的数据
    :param m:
    :return:
    """
    res=[]
    with open('recode.txt','r',encoding='utf-8') as f:
        data=f.readlines()
        if m>len(data):
            print('超出期数限制:{}期改为{}期'.format(m, len(data)))
            m=len(data)
    for i in range(-m,0):
        if data[i]=="\n": #去除空行
            continue
        res.append(data[i].strip().split('\t'))
    return res


def Recommend(data):
    """
    根据数据得出当前情况
    :param data:
    :return:
    """
    digitdic={str(i):0 for i in range(3,19)}
    remd={"大":0,"小":0,"单":0,"双":0}
    for i in range(len(data)):
        tem=data[i][-1].split(",")  #'11,大,单' ——> [11,大,单]
        digitdic[tem[0]]+=1
        remd[tem[1]]+=1
        remd[tem[2]]+=1
    return digitdic,remd

def getCurrentQihao():
    """
    得到当前期号
    :return:
    """
    with open(file_name,'r',encoding='utf-8') as f:
        data=f.readlines()
    return data[-1]

def getHe(data):
    """
    得到和值
    :param data:
    :return:
    """
    if data['大']==data['小'] and data['单']==data['双']:
        print('当期数为{}一致'.format(data['大']*2))
        return True

def drawFigureDaXiao(data):
    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #调节图像大小 宽高
    plt.figure(figsize=(3,3))
    labels =[u'大',u'小']
    plt.title("大小和值:"+str(data['大']+data['小']))
    sizes = [data['大'],data['小']]
    colors = ['red', 'yellowgreen']
    explode = (0.05, 0)
    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    #设置x y 轴一致
    plt.axis('equal')
    plt.legend()
    plt.show()


def drawFigureDaXiaoDanShuang(data):
    # 解决中文乱码
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #调节图像大小 宽高
    plt.figure(figsize=(3,3))
    labels =[u'单',u'双']
    plt.title("单双和值:"+str(data['单']+data['双']))
    sizes = [data['单'],data['双']]
    colors = ['red', 'yellowgreen']
    explode = (0.05, 0)
    patches, l_text, p_text = plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                                      labeldistance=1.1, autopct='%3.1f%%', shadow=False,
                                      startangle=90, pctdistance=0.6)
    # labeldistance，文本的位置离远点有多远，1.1指1.1倍半径的位置
    # autopct，圆里面的文本格式，%3.1f%%表示小数有三位，整数有一位的浮点数
    # shadow，饼是否有阴影
    # startangle，起始角度，0，表示从0开始逆时针转，为第一块。一般选择从90度开始比较好看
    # pctdistance，百分比的text离圆心的距离
    # patches, l_texts, p_texts，为了得到饼图的返回值，p_texts饼图内部文本的，l_texts饼图外label的文本

    #设置x y 轴一致
    plt.axis('equal')
    plt.legend()
    plt.show()

def drawHeatMap():
    import random
    from pyecharts import charts

    x_axis = [
        "12a", "1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p", "6p", "7p", "8p", "9p", "10p", "11p"]
    y_axis = [
        "Saturday", "Friday", "Thursday", "Wednesday", "Tuesday", "Monday", "Sunday"]
    data = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    heatmap = HeatMap()
    heatmap.add(
        "热力图直角坐标系",
        x_axis,
        y_axis,
        data,
        is_visualmap=True,
        visual_text_color="#000",
        visual_orient="horizontal",
    )
    heatmap.render()

def drawHeatMapBySeaborn(data):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    a = np.random.uniform(0, 1, size=(10, 10))
    sns.heatmap(a, cmap='Accent')
    plt.show()

def getOpenRes(data):
    """
    将 文件中数据拆分
    :param data:
    :return:
    """
    qihao=[]
    opencode=[]
    res=[]
    for i in range(len(data)):
        qihao.append(data[i][0])
        opencode.append(data[i][1])
        res.append(data[i][2].split(","))
    return qihao,opencode,res


def FindDrawgon(index=0):
    """
    查询最近几期连续的结果
    :param index:
    :return:
    """
    countDaXiao=1
    countDanShuang=1
    data = getAnylize(index)
    #数据倒叙排序以便发现龙
    print(data[::-1])
    qihao,opencode,data = getOpenRes(data[::-1])  #data=[[12,大，单],[13，小，双]]
    for i in range(1,len(data)-1):
        if data[0][1]==data[i+1][1]:
            countDaXiao+=1
        if data[0][2]==data[i+1][2]:
            countDanShuang+=1
        else:
            break
    return data[0][1],countDaXiao,data[0][2],countDanShuang

def getPicture(data):
    """
    画出大小单双分布图 并得到当前情况
    :return:
    """
    drawFigureDaXiao(data)
    drawFigureDaXiaoDanShuang(data)
    print("当前期数开奖情况：",getCurrentQihao())

def getMinAndMaxRange(qishu,minval,maxval):
    """
    得到已有数据中指定范围内百分比占比
    :param minval:
    :param maxval:
    :return:
    """
    count=0
    notcount=0
    data= getAnylize(qishu)
    digit, cmd = Recommend(data)
    print("各数字出现次数:", digit)
    print("大小单双分布情况:", cmd)
    qihao,opencode,res= getOpenRes(data)
    for i in range(len(res)):
        if minval<=int(res[i][0])<=maxval:
            count+=1
        else:
            notcount+=1
    print("范围为：%s - %s"%(minval,maxval))
    print("范围内",count)
    print("不在范围内",notcount)
    print("百分比",float(count/(notcount+count)))

def getDistribution(maxval,spcial=None):
    """
    :param maxval:
    :param spcial:
    :return:
    """
    mu,sigma =0,1 #正态分布中u = 0,sigma=1
    data=np.random.randint(4,18,100)
    plt.hist(data, bins=1000, normed=True)
    plt.show()
    return data


if __name__=="__main__":
    pass
    # data= getDistribution(100)

    # drawHeatMap()
    # drawHeatMapBySeaborn(1)


    # while True:
    #     res1,daxiaoDra,res2,danshaungDra=FindDrawgon(10)
    #     print(res1,daxiaoDra)
    #     print(res2,danshaungDra)
    #     time.sleep(30)


