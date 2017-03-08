#coding:utf8

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()   #未抓取的URL集合
        self.old_urls = set()   #已抓取的URL集合

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)  #如果URL不在待抓取的集合和已抓取的集合里，就将它添加到待抓取的集合里

    def add_new_urls(self, urls):   #增加新的URL到URL管理器
        if urls is None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self): #判断是否有新的URL
        return len(self.new_urls) != 0

    def get_new_url(self):  #获取待抓取的URL
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
