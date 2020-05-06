import requests
import js2py
from selenium import webdriver
import time


def verify_code():
    '''请求ajax所需cookie的生成'''

    js_content = js2py.EvalJs()
    js_content.execute('var n = (new Date).getTime().toString(36)')
    n = js_content.n
    js_code = ''' var t = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".split("")
                              , e = t.length
                              , n = (new Date).getTime().toString(36)
                              , r = [];
                            r[8] = r[13] = r[18] = r[23] = "_",
                            r[14] = "4";
                            for (var o, i = 0; i < 36; i++)
                                r[i] || (o = 0 | Math.random() * e,
                                r[i] = t[19 == i ? 3 & o | 8 : o]);'''

    js_content.execute(js_code)

    a = 'verify' + n + '_' + js_content.r.join('')

    return a


def Request(text1, headers, cookies):
    '''请求函数'''

    # 传入cookie去请求text1
    response = requests.get(text1, headers, cookies=cookies)

    response.encoding = 'utf-8'

    return response.text


def main():
    chrome_driver = '/Users/liangdingguan/.virtualenvs/spider/lib/python3.6/site-packages/selenium/webdriver/chrome/chromedriver'
    driver = webdriver.Chrome(executable_path=chrome_driver)
    driver.get('http://127.0.0.1:5000/')  # 请求flask 页面
    time.sleep(1)
    driver.refresh()  # 刷新一下
    text1 = driver.find_element_by_xpath('//*[@id="demo"]').text  # 获取flask页面中js数据 text1是加入参数后生成的url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'cookie': '__tasessionId=gr2kqu0r81587951527050'}

    # 调用 函数生成 ajax请求的cookie
    cookie = verify_code()
    cookies = {'s_v_web_id': cookie}  # 得到cookies

    # 调用请求函数发起请求
    v = Request(text1, headers, cookies)

    # 打印ajax请求的json结果
    print(v)


if __name__ == '__main__':
    main()





