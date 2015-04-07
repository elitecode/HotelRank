from scrapy.spider import Spider
from hotel.items import HotelItem
from scrapy.http import Request
import json

class tripadvisorSpider(Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.in"]
    fo = None
    reviewLinkList = []

    def start_requests(self):
        self.fo = open("reviewLinks.json","w")
        fi = open("city.json")
        hotel_list = json.load(fi)
        for d in hotel_list:
            data = hotel_list[d]
            url = ("http://www.tripadvisor.in/Search?q="+data['name']).replace(' ','+').replace('&','&amp;')
            data['name']=data['name'].encode('ascii','ignore')
            yield Request(url, lambda r, i=data['name']: self.parse(r, i))
        fi.close()

    def parse(self, response, name):
        link = HotelItem()
        link['name'] = name
        link['link'] = response.xpath('//div[@id="SEARCH_RESULTS"]//div[@class="searchResult srLODGING item1"]/div[@class="srHead"]/a/@href').extract()[0].encode("ascii","ignore")
        data = response.xpath('//div[@id="SEARCH_RESULTS"]//div[@class="searchResult srLODGING item1"]//div[@class="rating"]//a/text()').extract()
        data = [i.encode("ascii","ignore") for i in data]
        for n in data:
            if "review" in n:
                n = n.replace(',','')
                nReviews = [int(s) for s in n.split() if s.isdigit()]
                nReviews = nReviews[0]
        link['nReviews'] = nReviews
        self.reviewLinkList.append(dict(link))
        return link

    def closed(self, reason):
        self.fo.write(json.dumps(self.reviewLinkList))
        self.fo.close()
