#-*-coding:utf-8-*-
#lilybbs.py
#Author:Sky_Money
#Python实现自动登录BBS并发帖

import urllib,urllib2

#帐号和密码，你懂的
username=''
password=''

baseurl='http://bbs.nju.edu.cn/vd45734/bbslogin?type=2'
postdata=urllib.urlencode({
    'id':username,
    'pw':password,
    'lasturl':''})
req=urllib2.Request(
    url=baseurl,
    data=postdata)
result=urllib2.urlopen(req).read()

#从返回的Content中抓取Cookie
start=result.find("('")+2
end=result.find("')")
cookie=result[start:end]

split1=cookie.find('N')
split2=cookie.find('+')

u_num=int(cookie[0:split1])
u_id=cookie[split1+1:split2]
u_key=int(cookie[split2+1:])
footkey=217872412

#下面是发帖验证
testUrl='http://bbs.nju.edu.cn/vd78013/bbssnd?board=test'

sendCookie="_U_NUM=%d;_U_UID=%s;_U_KEY=%d;FOOTKEY=%d"%(u_num+2,u_id
                                                       ,u_key-2,footkey)
#发送的Headers，必须要有Cookie
sendheaders = {
        'Host': 'bbs.nju.edu.cn',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML,like Gecko) Chrome/15.0.874.121 Safari/535.2',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Accept-Charset': 'GBK,utf-8;q=0.7,*;q=0.3',
    }

sendheaders['Cookie']=sendCookie

#发帖的data主体
body=urllib.urlencode({'title':'test',
      'pid':'0',
      'reid':'0',
      'signature':'1',
      'autocr':'on',
      'text':'oh yeah'})
returnedReq=urllib2.Request(
    url=testUrl,
    data=body,
    headers=sendheaders)
returnedResult=urllib2.urlopen(returnedReq).read()
print returnedResult