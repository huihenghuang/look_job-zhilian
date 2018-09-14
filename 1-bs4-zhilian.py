import requests

from bs4 import BeautifulSoup

import json

import urllib.parse

url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'

# 参数
'''		data = {
			'jl': self.area,
			'kw': self.gangwei,
			'p': page
		}'''

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
           'Host':'sou.zhaopin.com',
           'Cookie':'dywem=95841923.y; zg_did=%7B%22did%22%3A%20%2215e6f3e027b280-0957e04dd7bd82-3f63450e-144000-15e6f3e027c845%22%7D; NTKF_T2D_CLIENTID=guest2017FE6E-3694-7339-7A82-58AEDD55E252; adfbid2=0; __utmv=269921210.|2=Member=1912450118=1; _jzqy=1.1513827229.1517965697.3.jzqsr=baidu.jzqsr=baidu|jzqct=%E6%99%BA%E8%81%94%E6%8B%9B%E8%81%98; JSSearchModel=0; campusOperateJobUserInfo=0948d75c-5645-4ca3-9229-1eb29d0887cf; zg_08c5bcee6e9a4c0594a5d34b79b9622a=%7B%22sid%22%3A%201528697211954%2C%22updated%22%3A%201528697212012%2C%22info%22%3A%201528697211956%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22sou.zhaopin.com%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fxiaoyuan.zhaopin.com%2Fjob%2FCC000930155J90000019000%3Fssidkey%3Dy%26ss%3D201%26ff%3D03%26sg%3Da7d638c8d0194d7d914e93a348023b35%26so%3D9%22%7D; _jzqa=1.1653535386403270000.1508291900.1529543073.1529891883.51; _jzqx=1.1508291900.1529891883.17.jzqsr=ts%2Ezhaopin%2Ecom|jzqct=/jump/index_new%2Ehtml.jzqsr=ts%2Ezhaopin%2Ecom|jzqct=/jump/index_new%2Ehtml; LastJobTag=%e4%ba%94%e9%99%a9%e4%b8%80%e9%87%91%7c%e5%b8%a6%e8%96%aa%e5%b9%b4%e5%81%87%7c%e8%8a%82%e6%97%a5%e7%a6%8f%e5%88%a9%7c%e7%bb%a9%e6%95%88%e5%a5%96%e9%87%91%7c%e5%ae%9a%e6%9c%9f%e4%bd%93%e6%a3%80%7c%e5%91%98%e5%b7%a5%e6%97%85%e6%b8%b8%7c%e5%bc%b9%e6%80%a7%e5%b7%a5%e4%bd%9c%7c%e9%a4%90%e8%a1%a5%7c%e5%b9%b4%e5%ba%95%e5%8f%8c%e8%96%aa%7c%e5%91%a8%e6%9c%ab%e5%8f%8c%e4%bc%91%7c%e8%a1%a5%e5%85%85%e5%8c%bb%e7%96%97%e4%bf%9d%e9%99%a9%7c%e4%ba%a4%e9%80%9a%e8%a1%a5%e5%8a%a9%7c%e9%80%9a%e8%ae%af%e8%a1%a5%e8%b4%b4%7c%e5%8a%a0%e7%8f%ad%e8%a1%a5%e5%8a%a9%7c%e5%88%9b%e4%b8%9a%e5%85%ac%e5%8f%b8%7c%e6%af%8f%e5%b9%b4%e5%a4%9a%e6%ac%a1%e8%b0%83%e8%96%aa%7c%e8%82%a1%e7%a5%a8%e6%9c%9f%e6%9d%83%7c%e5%85%a8%e5%8b%a4%e5%a5%96%7c%e5%b9%b4%e7%bb%88%e5%88%86%e7%ba%a2%7c%e5%85%8d%e8%b4%b9%e7%8f%ad%e8%bd%a6%7c14%e8%96%aa%7c%e9%ab%98%e6%b8%a9%e8%a1%a5%e8%b4%b4%7c%e5%8c%85%e5%90%83%7c%e5%8c%85%e4%bd%8f%7c%e5%81%a5%e8%ba%ab%e4%bf%b1%e4%b9%90%e9%83%a8%7c%e4%b8%8d%e5%8a%a0%e7%8f%ad%7c%e4%bd%8f%e6%88%bf%e8%a1%a5%e8%b4%b4%7c%e6%88%bf%e8%a1%a5%7c%e6%97%a0%e8%af%95%e7%94%a8%e6%9c%9f%7c%e9%87%87%e6%9a%96%e8%a1%a5%e8%b4%b4%7c%e5%85%8d%e6%81%af%e6%88%bf%e8%b4%b7; LastSearchHistory=%7b%22Id%22%3a%22b45a32a7-3ffb-45dc-a802-6efdefc02b69%22%2c%22Name%22%3a%22python+%2b+%e4%b8%8a%e6%b5%b7%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e4%25b8%258a%25e6%25b5%25b7%26kw%3dpython%26sm%3d0%26ispts%3d1%26isfilter%3d1%26p%3d1%22%2c%22SaveTime%22%3a%22%5c%2fDate(1529891916079%2b0800)%5c%2f%22%7d; _qzja=1.546852014.1513168714274.1529543079839.1529891891874.1529891910270.1529891914464.0.0.0.201.40; urlfrom2=121113803; sts_deviceid=1644ade919f62b-0c98b56ecbd29b-3961430f-1327104-1644ade91a06aa; ZP_OLD_FLAG=false; urlfrom=121113803; adfbid=0; adfcid=pzzhubiaoti1; adfcid2=pzzhubiaoti1; __utma=269921210.1428116669.1508291899.1530264452.1530494100.82; __utmc=269921210; __utmz=269921210.1530494100.82.49.utmcsr=other|utmccn=121113803|utmcmd=cnt|utmctr=%E6%99%BA%E8%81%94; __xsptplus30=30.48.1530494100.1530494100.1%231%7Cother%7Ccnt%7C121113803%7C%7C%23%23qJvahCZ1gjEHozYP3GGpDkFa9mN39mTi%23; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1529543066,1529891882,1530264452,1530494100; dywea=95841923.2099730433246266600.1508291895.1530264450.1530494101.80; dywec=95841923; dywez=95841923.1530494101.80.48.dywecsr=other|dyweccn=121113803|dywecmd=cnt|dywectr=%E6%99%BA%E8%81%94; sts_sg=1; sts_sid=164588eca8767b-0303f4ee631da1-3961430f-1327104-164588eca888a9; zp_src_url=http%3A%2F%2Fts.zhaopin.com%2Fjump%2Findex_new.html%3Futm_source%3Dother%26utm_medium%3Dcnt%26utm_term%3D%26utm_campaign%3D121113803%26utm_provider%3Dzp%26sid%3D121113803%26site%3Dpzzhubiaoti1; __utmb=269921210.2.10.1530494100; ZP-ENV-FLAG=gray; dyweb=95841923.2.10.1530494101; Hm_lvt_d838d7d6abb840b6c1a339ec5aee915d=1530264471,1530494129; __ads_session=SbXtPVJZHwl7s+VCQgA=; GUID=c2f910a318714fdaa05c444ed9fe4d50; Hm_lpvt_d838d7d6abb840b6c1a339ec5aee915d=1530494263; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1530494263; LastCity=%E4%B8%8A%E6%B5%B7; LastCity%5Fid=538; ZL_REPORT_GLOBAL={%22sou%22:{%22actionIdFromSou%22:%229e6ef318-7fe5-4666-bdbf-26d3587e2aaf-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=13'}

class ZhilianCrawl(object):

    def __init__(self,page,key):
        super().__init__()
        self.page = page
        self.key = key
        self.items = []

    #     启动爬虫
    def start_crawl(self):
        for p in range(1,self.page+1):
            params = {'jl':'上海',
                      'kw':self.key,
                      'p':p}
            params = urllib.parse.urlencode(params)

            url_job = url+params

            response = requests.get(url=url_job,headers = headers,verify = False)
            response.encoding='utf-8'
            html = response.text
#             解析
            self.parse(html)

    #     保存数据
        self.write2file()

    def parse(self, html):

        soup = BeautifulSoup(html, 'lxml')

        tables = soup.find(name='div', attrs={'class': 'newlist_list_content'}).find_all('table',
                                                                                           attrs={'class': 'newlist'})
        # print(len(tables))
        #
        # print(tables[10])

        for table in tables[1:]:

            salary = table.find('td',class_ = 'zwyx').get_text()
            gzdd_ = table.select('td.gzdd')[0]
            print(gzdd_)
            address = gzdd_.string

            company = table.select('td.gsmc > a')[0].get_text()

            job_ = table.select('td.zwmc > div > a')[0]
            job = job_.get_text()

            item  = {}
            item['salary'] = salary
            item['address'] = address
            item['company'] = company
            item['job'] = job

            self.items.append(item)

    def write2file(self):
        with open('./智联招聘.json',mode='w',encoding='utf-8') as fp:
#             self.items 列表
            str = json.dumps(self.items,ensure_ascii=False)
            fp.write(str)
            print('数据保存成功！')
if __name__ == '__main__':
    page = int(input('请输入查询多少页：'))

    key = input('请输入工作类型：')

    # 创建一个类，爬虫功能，进行封装
    zhilian = ZhilianCrawl(page,key)

    # 调用对象方法，启动爬虫
    zhilian.start_crawl()