# -*- coding: utf-8 -*-

from os import environ
#from google.appengine.api import app_identity

is_debug = environ.get("SERVER_SOFTWARE", "").startswith("Development/")

SITE_TITLE = "SAEspot" #

ADMIN_MAIL = "xxxxx@gmail.com"

ONLY_USE_MAJOR_DOMAIN = not is_debug

#放在网页底部的统计代码
ANALYTICS_CODE = ""

#APPID = app_identity.get_application_id()
#MAJOR_DOMAIN = '%s.appspot.com'%APPID
MAJOR_DOMAIN = 'www.xxx.com'

if is_debug:
    BASE_URL = 'http://127.0.0.1:8080'
else:
    BASE_URL = 'http://%s'%MAJOR_DOMAIN

THEME = 'default'

if is_debug:
    JQUERY = "/static/js/jquery-1.6.4.js"
else:
    JQUERY = "/static/js/jquery-1.6.4.js"
    #JQUERY = "http://ajax.googleapis.com/ajax/libs/jquery/1.5.2/jquery.min.js"
    #JQUERY = "http://code.jquery.com/jquery-1.6.2.min.js"

LINK_BROLL = [
    {'text': 'youBBS', 'url': 'https://www.youbbs.org/', 'title': u'超轻量级论坛'},
]

#下面的设置比较合理，建议不要修改
TITLE_MAX_S = 60 #帖子标题最多字数
CONTENT_MAX_S = 2000 #帖子内容最多字数
COMMENT_MAX_S = 1200 #回复内容最多字数
RECENT_POST_NUM = 20 #首页显示的文章数
EACH_PAGE_POST_NUM = 20 #每页显示文章数
EACH_PAGE_COMMENT_NUM = 32 #每页评论数
DESCRIPTION_CUT_WORDS = 100 #meta description 显示的字符数
RECENT_COMMENT_NUM = 10 #边栏显示最近被评论的帖子数
FEED_NUM = 10 #订阅显示的文章数，要小于RECENT_POST_NUM
MEMBER_RECENT_TOPIC = 10 #记录个人最近的发帖数
MEMBER_RECENT_REPLY = 10 #记录个人最近的回帖数
NOTIFY_NUM = 16 #最多提醒条数
NOTIFY_MEMBER_NUM = 10 #一个帖子或回复可允许最多 @username 的人数
DEFAULT_CACHE_TIME = 600 #默认的缓存时间 n秒

##upyun
UPYUN_USER = 'saespotuserxxx'
UPYUN_PW = 'xxxxxxxx'
#头像图片
DOMAIN_NAME_AVATAR = 'saespot'
AVATAR_URL = 'http://%s.b0.upaiyun.com/avatar/'%DOMAIN_NAME_AVATAR

#图片上传
DOMAIN_NAME_UPLOAD = 'saespots'
UPLOAD_URL = 'http://%s.b0.upaiyun.com'%DOMAIN_NAME_UPLOAD
