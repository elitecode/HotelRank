from scrapy.spider import Spider
from scrapy.http import Request
from hotel.items import ReviewItem
import json, math

class tripadvisorreviewsSpider(Spider):
	name = "tripadvisorreviews"
	allowed_domains = ["tripadvisor.in"]
	hotelReviewList = {}
	fo = None
	# link="http://www.tripadvisor.in/Hotel_Review-g304551-d1415547-Reviews-Hotel_Hari_Piorko-New_Delhi_National_Capital_Territory_of_Delhi.html"
	# link_base= link.split('Reviews',1);
	# link_base[0]=link_base[0]+"Reviews"
	# links_final=[]
	# k=3 # if its last page number is k then
	# for i in range(1,k+1):
	# 	if(i==1):
	# 		links_final.append(link_base[0]+link_base[1])
	# 	else:
	# 		links_final.append(link_base[0]+"-or"+str(10*(i-1))+link_base[1])	
	# print links_final
	# start_urls = links_final

	def start_requests(self):
		self.fo = open("reviews.json","w")
		fi = open("reviewLinks.json","r")
		hotel_list = json.load(fi)
		for data in hotel_list:
			k = data['nReviews']
			self.hotelReviewList[data['name']] = {}
			self.hotelReviewList[data['name']]['name'] = [data['name']]
			self.hotelReviewList[data['name']]['reviews'] = []
			self.hotelReviewList[data['name']]['count'] = 0
			link = "http://www.tripadvisor.com" + data['link']
			link_base= link.split('Reviews',1)
			link_base[0]=link_base[0]+"Reviews"
			links_final=[]
			k = int(math.floor(k/10))
			if k > 33:
				k=33
			for i in range(1,k+1):
				if(i==1):
					yield Request(link_base[0]+link_base[1], lambda r: self.parse(r, data['name']))
				else:
					yield Request(link_base[0]+"-or"+str(10*(i-1))+link_base[1], lambda r: self.parse(r, data['name']))
		fi.close()

	def parse(self, response, name):
		items=[]
		output=response.xpath('//p[@class="partial_entry"]/text()').extract()
		output = [ o.encode('ascii','ignore') for o in output]

		for i in output:
			item = ReviewItem()
			if (len(i) > 10):
				item['review']=i
				self.hotelReviewList[name]['reviews'].append(i.encode('ascii','ignore'))
				self.hotelReviewList[name]['count'] += 1
				# self.reviewList[name]
				# self.fo.write(i)
				items.append(item)
		return items

	def closed(self, reason):
		self.fo.write(json.dumps(self.hotelReviewList))
		self.fo.close()