#!/usr/bin/env python3

from libs.logger import logger
from libs.check import is_available
from libs.wechat import send_wechat_msg


def main():
    domain='example.com'
    available = is_available(domain)
    # send_wechat_msg('wechatID|wechatID|wechatID', 'Title', 'Content')
    if available:
        send_wechat_msg('wechatID', 'Domain registration notice', 'example.com is available')

if __name__ == '__main__':
    main()
