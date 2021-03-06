# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 下午2:37
# @Author  : zhouzz
# @FileName: postTest.py

import requests
#先打开登录首页，获取部分cookie
url = "https://passport.cnblogs.com/user/signin"
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
           }
s = requests.session()
r = s.get(url, headers=headers,verify=False)
print r.status_code
print s.cookies

# 添加登录需要的两个cookie
c = requests.cookies.RequestsCookieJar()

c.set('.CNBlogsCookie', '这里是抓到的')  # 填上面抓包内容
c.set('.Cnblogs.AspNetCore.Cookies','这里是抓到的')  # 填上面抓包内容
c.set('AlwaysCreateItemsAsActive',"True")
c.set('AdminCookieAlwaysExpandAdvanced',"True")
s.cookies.update(c)
print s.cookies

# 登录成功后保存编辑内容
r1 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1", headers=headers, verify=False)

# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR": "FE27D343",
        "Editor$Edit$txbTitle": "这是3111",
        "Editor$Edit$EditorBody": "<p>这里111：http://www.cnblogs.com/yoyoketang/</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage": "on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$Advanced$txbEntryName": "",
        "Editor$Edit$Advanced$txbExcerpt": "",
        "Editor$Edit$Advanced$tbEnryPassword": "",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print r.content