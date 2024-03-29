#获取计划的预测值
import time
import requests
import json

url = "http://9x904.com/api/Plan/getPlan"
typeid = 65   #急速为65
groupid= 39
danShuang= 1   #1代表单双 2代表大小
daXiao= 2
count_res=1

headers= {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '29',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'PHPSESSID=mp9o82vks0fo1u77coevct33i7; username=libuda; nickname=%E7%AD%BE%E6%8A%95%E6%83%8A%E7%90%85; roomId=81259577540609; vocabulary=%E6%93%8D%E4%BD%A0%E5%A6%88%EF%BC%8C%E6%BB%9A%EF%BC%8C%E5%82%BB%E9%80%BC%EF%BC%8C%E4%BD%A0%E5%A6%88%E9%80%BC%EF%BC%8C%E5%9E%83%E5%9C%BE%EF%BC%8C%E5%9D%91%E4%BA%BA%EF%BC%8C%E5%9D%91%E7%88%B9%EF%BC%8C%E5%9D%91%E9%92%B1%EF%BC%8C%E5%B9%B3%E5%8F%B0%EF%BC%8C%E5%A6%88%E5%8D%96%E6%89%B9; td_cookie=353993934; token=f4f7654b442623ddb4be1ad54264e206; RoomIdData={%22groupNumber%22:%2211%22%2C%22isRegister%22:%221%22%2C%22administration%22:%220%22%2C%22startTime%22:%22%22%2C%22endTime%22:%22%22%2C%22ChatUserLevel%22:%222%22%2C%22anexcuse%22:%221%22%2C%22videoPlay%22:%221%22%2C%22videoLink%22:%22%22%2C%22videoGrade%22:%221%22%2C%22notePopupAmount%22:%22666%22%2C%22ChatSwitch%22:%221%22%2C%22planSwitch%22:%221%22%2C%22rankingList%22:%221%22%2C%22LongDragon%22:%221%22%2C%22rewardSwitch%22:%220%22}',
    'Host': '9x904.com',
    'Origin': 'http://9x904.com',
    'Referer': 'http://9x904.com/mobile/new_pc_1/index.html',
    'sign': '2E27994045F972DEC868E5791E5C28D7',
    'timestamp': str(int(time.time())),    #这里的时间戳为当前时间
    'token': 'f4f7654b442623ddb4be1ad54264e206',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
}
#单双预测
data1={
    'typeId': typeid,
    'groupId': groupid,
    'suffix': danShuang,
}

#大小预测
data2={
    'typeId': typeid,
    'groupId': groupid,
    'suffix': daXiao,
}

def getPre():
    """
    返回预测期数与预测结果
    :return:
    """
    global count_res
    data=requests.post(url=url,data=data1,json=True,headers=headers)
    data=json.loads(data.text)
    #预测结果中第一个正在预测 第二个为上次预测情况

    now_prediction=data['data'][0]['prediction'] #当前预测结果
    flag=True      #代表是否是最近几期预测情况

    res = data['data'][1]['result']  #最近一期的预测对错
    for one in data['data'][2:]:
        if flag:
            if one['result'] == res:
                count_res+=1
            else:
                count_res=1
                flag=False
        break
    print("老马狗连续预测 %s %s 期啦！赶紧决定！"%(res,count_res))
    return now_prediction,count_res

def xiaZhu(money):
    post_url = "http://9x904.com/api/game/postCodeWeb"
    post_headers ={
        'Host':'9x904.com',
        'Connection':'keep-alive',
        'Content-Length':'326',
        'Origin': 'http://9x904.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json, text/plain, */*',
        'timestamp': str(int(time.time())),
        'token': '77fa84646c0bc5410c999f192a519470',
        'sign':'3E476407B34A8EBE92BCF1614FC9FE0C',
        'Referer':'http://9x904.com/mobile/new_pc_1/index.html',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':'PHPSESSID=be4vd288v2b3e2vj21o17c0s27; username=libuda; nickname=%E7%AD%BE%E6%8A%95%E6%83%8A%E7%90%85; roomId=81259577540609; vocabulary=%E6%93%8D%E4%BD%A0%E5%A6%88%EF%BC%8C%E6%BB%9A%EF%BC%8C%E5%82%BB%E9%80%BC%EF%BC%8C%E4%BD%A0%E5%A6%88%E9%80%BC%EF%BC%8C%E5%9E%83%E5%9C%BE%EF%BC%8C%E5%9D%91%E4%BA%BA%EF%BC%8C%E5%9D%91%E7%88%B9%EF%BC%8C%E5%9D%91%E9%92%B1%EF%BC%8C%E5%B9%B3%E5%8F%B0%EF%BC%8C%E5%A6%88%E5%8D%96%E6%89%B9; td_cookie=4123598824; token=77fa84646c0bc5410c999f192a519470; RoomIdData={%22groupNumber%22:%2211%22%2C%22isRegister%22:%221%22%2C%22administration%22:%220%22%2C%22startTime%22:%22%22%2C%22endTime%22:%22%22%2C%22ChatUserLevel%22:%222%22%2C%22anexcuse%22:%221%22%2C%22videoPlay%22:%221%22%2C%22videoLink%22:%22%22%2C%22videoGrade%22:%221%22%2C%22notePopupAmount%22:%22666%22%2C%22ChatSwitch%22:%221%22%2C%22planSwitch%22:%221%22%2C%22rankingList%22:%221%22%2C%22LongDragon%22:%221%22%2C%22rewardSwitch%22:%220%22}',
    }
    post_data ={
        'code[0][actionNum]': '1',
        'code[0][playedGroup]': '39',
        'code[0][beiShu]': '1',
        'code[0][orderId]': '231668192081',
        'code[0][actionData]': 'k3hz_shuang',
        'code[0][playedId]': '118',
        'code[0][type]': '60',
        'para[actionNo]': '190927131',
        'para[kjTime]': '1569552600',
        'para[type]': '60',
        'zhongduan': '0',
        'zhuidata':'',
         'zhuihao': '0'
    }
    data = requests.post(url=post_url,data=post_data,headers=post_headers).json()
    return data

if __name__=="__main__":


    import datetime
    while 1:
        tm = datetime.datetime.now().second
        if 5 <= tm <= 10:
            now_prediction,count_res=getPre()
            print("当前预测",now_prediction)
            if count_res >= 6:
                yes = input("是否进行投注?")
                if yes=="y":
                    money = input("请输入投注金额")
                    res = xiaZhu(money)
                    print(res)
                else:
                    count_res=1
                    continue
            else:
                continue
            time.sleep(55)
        else:
            time.sleep(1)