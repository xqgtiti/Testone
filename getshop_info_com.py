# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from selenium.webdriver.chrome.options import Options
import platform
import random
import requests
#from xvfbwrapper import Xvfb
import logging.handlers
import sys
from multiprocessing.dummy import Pool
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium.common.exceptions import NoSuchElementException
import os
XH = 1
handler = logging.handlers.RotatingFileHandler('log_shop_%d.txt' % (XH), maxBytes=1024 * 1024 * 1024 * 1024,
                                               backupCount=10)  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter
logger = logging.getLogger('logging')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)
logger.info('first info message')
def get_shop(xh,id):
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"

    # 代理隧道验证信息
    proxyUser = "HG1407C5S46VG08D"
    proxyPass = "A4B4FDDB33090CBB"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    print str(xh) + ',' + str(id)
    flag = 0
    USER_AGENT_LIST = [

        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "WeChat/6.3.21.16 CFNetwork/758.4.3 Darwin/15.5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
        "Dalvik/1.6.0 (Linux; U; Android 4.0.3 Build/BesTV_Mozart_SH_1.9.2.34)",
        "Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0",
        "Dalvik/1.6.0 (Linux; U; Android 4.4.2; HG680 Build/1.3.5)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.3.21 NetType/WIFI Language/zh_CN",
        "Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko",
        "WeChat/6.3.21.16 CFNetwork/758.2.8 Darwin/15.0.0",
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Dalvik/1.6.0 (Linux; U; Android 4.4.2; B860A Build/2.3.2)",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13F69 Safari/601.1",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)"

    ]
    SHOP_URL = 'http://www.dianping.com/shop/%s' % id
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        "Pragma": "http://www.dianping.com/shop/",
        'Accept-Encoding': 'gzip, deflate',
        "X-Requested-With": "XMLHttpRequest",
        'Accept-Language': 'zh-CN,zh;q=0.8',
        "Cache-Control": "no-cache",
        'User-Agent': USER_AGENT_LIST[random.randint(0, 23)],
        'Upgrade-Insecure-Requests': '1'
    }
    cye_list = ['shanghai','beijing','zhenjiang','shenyang','guangzhou','hangzhou']
    cy_list = ['1','2','98','18','4','3']
    cookies = {}
    rand_number = random.randint(0,5)
    cookies['cye'] = cye_list[rand_number]
    cookies['cy'] = cy_list[rand_number]
    save_path = ""
    if platform.system() == 'Windows':
        save_path = 'F:\dianping//next_need_shop_data//%s.txt' % str(id)
    elif platform.system() == 'Linux':
        save_path = '/home/need_shop_data/%s.txt' % str(id)
    for i in range(0, 10):
        try:
            res = requests.get(SHOP_URL, headers=HEADERS, timeout=15, cookies=cookies,verify=False)
            if res.status_code == 200:
                html = res.text
                fsave = open(save_path, 'w')
                fsave.write(html)
                fsave.close()
                logger.info('save ok! %s'%str(id))
                print 'save ok! %s'%str(id)
                flag = 1
                break
            else:
                logger.info('get html fail,code%s, again...' % str(res.status_code))
                print 'get html fail,code%s, again...' % str(res.status_code)
                if res.status_code == 403:
                    print '403, sleep...'
                    logger.info('403, sleep...')
                elif res.status_code == 404:
                    print '404 break...'
                    logger.info('404, break')
                    break
                else: gd = 1
                time.sleep(3)
                continue
        except Exception as e:
            logger.info('time out, again....')
            print 'time out, again....'
            time.sleep(3)
            continue
    time.sleep(3)
def get_shop_driver(id):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    if platform.system() == 'Windows':
        save_path = 'F:\dianping/next_need_shop_data//%s.txt' % str(id)
        shop_success_path = 'F:\dianping//next_shop_success.txt'
    elif platform.system() == 'Linux':
        save_path = '/home/next_need_shop_data/%s.txt' % str(id)
        shop_success_path = '/home/next_shop_success.txt'
    driver = webdriver.Chrome(chrome_options=chrome_options)
    for i in range(0,5):
        try:
            driver.get('http://www.dianping.com/shanghai/food')
            driver.get('http://www.dianping.com/shop/%s'%id)
            break
        except:
            print 'get fail, try again....'
            continue
    try:
        WebDriverWait(driver,10,0.5).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'rights')))
        html = driver.page_source
        fsave = open(save_path, 'w')
        fsave.write(html)
        fsave.close()
        logger.info('save ok!')
        print 'save ok!'
        fsave2 = open(shop_success_path,'a')
        succ_table = {}
        succ_table['shopId'] = id
        fsave2.write(json.dumps(succ_table,ensure_ascii=False)+'\n')
        fsave2.close()
        driver.quit()
        return 1
    except:
        logger.info('get html fail!')
        print 'get html fail!'
        driver.quit()
        return 0
if __name__ == '__main__':
    """
    if platform.system() == 'Linux':
        vdisplay = Xvfb()
        vdisplay.start()
    """
    shop_id_list_path = ""
    if platform.system() == 'Windows':
        shop_id_list_path = 'F:\dianping\simple_shop_data\id_list_type//next_need_shop_list.txt'
        shop_success_path = 'F:\dianping//next_shop_success.txt'
        pre_path = 'F:\dianping//next_need_shop_data'
    elif platform.system() == 'Linux':
        shop_id_list_path = '/home/next_need_shop_list.txt'
        shop_success_path = '/home/next_shop_success.txt'
        pre_path = '/home/next_need_shop_data'

    preShop = {}
    f = open(shop_success_path,'rb')
    while True:
        r = f.readline()
        if not r: break
        r = r[:-1]
        r = r.strip('\r')
        res = eval(r)
        shop_id = res['shopId']
        preShop[shop_id] = 1
    f.close()

    f = open(shop_id_list_path, 'rb')
    shop_id_list = []
    cnt = 0
    while True:
        r = f.readline()
        if not r: break
        cnt = cnt + 1
        if cnt < (XH-1)*2500: continue
        if cnt >= XH*2500: continue
        print cnt
        r = r[:-1]
        r = r.strip('\r')
        res = eval(r)
        shopId = res['shopId']
        shop_id_list.append(shopId)

    for i in range(0,len(shop_id_list)):
        try:
            if preShop[shop_id_list[i]] == 1:
                print 'skip...'
                continue
        except: gd = 1
        get_shop_driver(shop_id_list[i])