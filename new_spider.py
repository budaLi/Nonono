import requests
import json
import time
import datetime
from matplotlib import pyplot as plt



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

def drawFigure(data):
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
if __name__=="__main__":
    # while True:
    #     # 35-40s结果肯定出来
    #     tm = datetime.datetime.now().second
    #     if 5 <= tm <= 10:
    #         response = requests.get(url=url, headers=headers)
    #         text = json.loads(response.text)
    #         res = text['data'][0]  # 最近一期
    #         print(res)
    #         # print(res)
    #         qihao = res['expect']  # 期号
    #         opencodearr = res['opencodearr']
    #         opencodearr = opencodearr.split(',')
    #         if qihao not in dic:
    #             dic[qihao] = res['opencode']
    #         else:  # 可能未开奖
    #             continue
    #         if opencodearr[1] == "大":
    #             flag1 += 1
    #         else:
    #             flag2 += 1
    #         if opencodearr[2] == "单":
    #             flag3 += 1
    #         else:
    #             flag4 += 1
    #         end = time.time()
    #         with open('recode.txt', 'a', encoding="utf-8") as f:
    #             if int(res['expect'])%10==0:  #十期空行
    #                 f.write("\n")
    #             f.write(qihao + "\t" + res['opencode'] + "\t" + ",".join(opencodearr) + "\n")
    #         print("当前形势为:期号:\033[1;45m{}\033[0m,大：\033[1;45m{}\033[0m,小：\033[1;45m{}\033[0m，"
    #               "单：\033[1;45m{}\033[0m,双：\033[1;45m{}\033[0m".format(qihao, flag1, flag2, flag3, flag4))
    #         time.sleep(55)
    #     else:
    #         time.sleep(1)
    for i in range(20,100000,10):
        data=getAnylize(i)
        digit, data=Recommend(data)
        print("各数字出现次数:",digit)
        print("大小单双分布情况:",data)
        # while True:
        #     if getHe(data):
        #         with open('hezhi.txt','w') as f:
        #             f.write()
        drawFigure(data)
        print("当前期数开奖情况：",getCurrentQihao())

