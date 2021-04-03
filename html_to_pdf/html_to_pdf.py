#!/usr/bin/python3

# from https://www.cnblogs.com/new-june/p/14509601.html
# from https://www.cnblogs.com/new-june/p/14509601.html
# from https://www.cnblogs.com/new-june/p/14509601.html

import os,json,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,

    # "customMargins": {},
    # "marginsType": 2,
    # "scaling": 100,
    # "scalingType": 3,
    # "scalingTypePdf": 3,
    "isLandscapeEnabled":False,#landscape横向，portrait 纵向，若不设置该参数，默认纵向
    "isCssBackgroundEnabled": True,
    "mediaSize": {
        "height_microns": 297000,
        "name": "ISO_A4",
        "width_microns": 210000,
        "custom_display_name": "A4 210 x 297 mm"
    },
}

chrome_options.add_argument('--enable-print-browser')
#chrome_options.add_argument('--headless') #headless模式下，浏览器窗口不可见，可提高效率

prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': 'your file path' #此处填写你希望文件保存的路径
}
chrome_options.add_argument('--kiosk-printing') #静默打印，无需用户点击打印页面的确定按钮
chrome_options.add_experimental_option('prefs', prefs)


# 需要将chromedriver换成相应平台下的chromedriver
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.maximize_window()

fname = 'interpreter_part_'
f = open('url.txt', 'r')
urls = f.read()
for url in urls.split('\n'):
    if len(url) == 0:
        break
    driver.get(url)
    # 这里可以用 js 的 document.title="filename.pdf" 修改html标题名称,该名称最后就是文件名
    script = 'window.print();'
    driver.execute_script(script)
f.close()
driver.close()
