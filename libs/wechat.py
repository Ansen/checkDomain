from urllib import request
import json

from libs.logger import logger
from config import corpid, corpsecret, wechat_party_id, wechat_agent_id
from time import localtime, strftime

def get_token():
    get_token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_content = request.urlopen(get_token_url)
    except request.HTTPError as e:
        logger.info(e.code)
        logger.info(e.read().decode("utf8"))
        exit()
    token_data = token_content.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token
 
def send_data(access_token,user,subject,content):
    timestr = strftime("%Y-%m-%d %H:%M:%S", localtime()) 
    wechat_api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    params = {
        "touser": user,
        "toparty":wechat_party_id,
        "msgtype":"textcard",
        "agentid":wechat_agent_id,
        "textcard":{
            "title" : subject,
            "description": "<div class=\"gray\">{}</div><div class=\"highlight\">{}</div>".format(timestr, content),
            "url": "None"
           },
        "safe":"0"
        }
    send_data = json.dumps(params, ensure_ascii=False).encode('utf-8')
    send_request = request.Request(url=wechat_api, data=send_data, method="POST")
    response = json.loads(request.urlopen(send_request).read().decode('utf-8'))
    logger.info(str(response))
 
 
def send_wechat_msg(user, subject, content):
    accesstoken = get_token()
    send_data(accesstoken, user, subject, content)
