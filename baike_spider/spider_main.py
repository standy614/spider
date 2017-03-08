#coding:utf8
import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        #初始化需要的各种对象
        self.urls = url_manager.UrlManager()    #URL管理器对象
        self.downloader = html_downloader.HtmlDownloader()  #网页下载器对象
        self.parser = html_parser.HtmlParser()  #网页解析器对象
        self.outputer = html_outputer.HtmlOutputer()    #网页输出器对象

    def craw(self,root_url):
        count = 1   #抓取次数
        self.urls.add_new_url(root_url) #入口URL
        while self.urls.has_new_url():  #如果有待爬取的URL
            try:
                new_url = self.urls.get_new_url()   #取出要爬取的URL
                print 'craw %d : %s'%(count, new_url)
                html_content = self.downloader.download(new_url)  #下载页面
                new_urls, new_data = self.parser.parser(new_url,html_content)    #将下载的页面进行解析并得到新的URL
                self.urls.add_new_urls(new_urls)    #将上面解析得到的新的URL补充到URL管理器
                self.outputer.collect_data(new_data)    #将解析到的页面数据进行收集

                if count == 10:
                    break
                count = count + 1
            except:
                print 'craw failed'
        self.outputer.outputer_html()

if __name__=="__main__":
    #爬虫入口
    root_url = "http://baike.baidu.com/link?url=7L07DCnaEx3rxJdY7KS20__krtoVBsQGw_J1kTm-tnyYikANFVar2IxR674aST3TkwLeb0lNNV2yChWZS0FU-_"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)