#测试多少次之后会失败
#导入随机数模块
import random

chishi=10
win=0
countKaijiang= 100  #开奖次数
init_benjin = 1000  #本金
init_zhichu = 10   #初始倍投金额

#设置一组十次的随机数，0为负，1为胜
def getAnswers(cishu):
    answers=[]
    while cishu:
        x = random.randint(0,1)
        answers.append(x)
        cishu-=1
    return answers

#设置下注函数，参数分别为 本金，支出，随机值列表，输赢变量
def BeginGame(benjin,zhichu,answer,win):
    """
    根据当前本金、投注及输赢结果求出本次本金结余
    :param benjin:
    :param zhichu:
    :param answer:
    :param win:
    :return:
    """
    if answer==0:
        benjin-=zhichu
        zhichu*=2
        win+=1  #表示连输一次
    else:
        benjin+=zhichu*1.7
        zhichu=chishi
        win=0
    return benjin,zhichu,win

if __name__=="__main__":
    answers = getAnswers(countKaijiang)
    print("输赢占比: 输 %s  赢 %s" % (answers.count(1) / len(answers), 1 - answers.count(1) / len(answers)))
    # print(answers)
    playcount=0
    for one in answers:
        init_benjin, init_zhichu,win=BeginGame(init_benjin,init_zhichu,one,win)
        if init_benjin<=0:
            print("经过%s次输光本金"%playcount,"连输%s次"%win)
            break
        else:
            playcount += 1
            print("本金%s"%init_benjin)
