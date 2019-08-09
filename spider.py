import requests
import json
import time
import datetime
# 爬虫地址
url = 'http://9x904.com/api/game/k3OpenList?lotteryid=65'

# 携带cookie进行访问
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
   'Cookie': 'td_cookie=3606231329; PHPSESSID=95hjt64h922bvlk1i77afhohr1; username=libuda; nickname=%E7%AD%BE%E6%8A%95%E6%83%8A%E7%90%85; roomId=81259577540609; vocabulary=%E6%93%8D%E4%BD%A0%E5%A6%88%EF%BC%8C%E6%BB%9A%EF%BC%8C%E5%82%BB%E9%80%BC%EF%BC%8C%E4%BD%A0%E5%A6%88%E9%80%BC%EF%BC%8C%E5%9E%83%E5%9C%BE%EF%BC%8C%E5%9D%91%E4%BA%BA%EF%BC%8C%E5%9D%91%E7%88%B9%EF%BC%8C%E5%9D%91%E9%92%B1%EF%BC%8C%E5%B9%B3%E5%8F%B0%EF%BC%8C%E5%A6%88%E5%8D%96%E6%89%B9',
    'Host': '9x904.com',
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
    with open('recode.txt','r') as f:
        lines = len(f.readlines())

if __name__=="__main__":
    while True:
        # 35-40s结果肯定出来
        tm = datetime.datetime.now().second
        if 5 <= tm <= 10:
            response = requests.get(url=url, headers=headers)
            text = json.loads(response.text)
            res = text['data'][0]  # 最近一期
            print(res)
            # print(res)
            qihao = res['expect']  # 期号
            opencodearr = res['opencodearr']
            opencodearr = opencodearr.split(',')
            if qihao not in dic:
                dic[qihao] = res['opencode']
            else:  # 可能未开奖
                continue
            if opencodearr[1] == "大":
                flag1 += 1
            else:
                flag2 += 1
            if opencodearr[2] == "单":
                flag3 += 1
            else:
                flag4 += 1
            end = time.time()
            with open('recode.txt', 'a', encoding="utf-8") as f:
                if int(res['expect'])%10==0:  #十期空行
                    f.write("\n")
                f.write(qihao + "\t" + res['opencode'] + "\t" + ",".join(opencodearr) + "\n")
            print("当前形势为:期号:\033[1;45m{}\033[0m,大：\033[1;45m{}\033[0m,小：\033[1;45m{}\033[0m，"
                  "单：\033[1;45m{}\033[0m,双：\033[1;45m{}\033[0m".format(qihao, flag1, flag2, flag3, flag4))
            time.sleep(55)
        else:
            time.sleep(1)