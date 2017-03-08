#coding:utf8
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None #如果链接是空的，则返回空的内容
        response = urllib2.urlopen(url) #否则将网页内容存储在response

        if response.getcode() != 200:
            return None #如果状态码不是200，则返回空内容
        return response.read()  #否则返回网页内容