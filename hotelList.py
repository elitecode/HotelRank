import json,os
import urllib2

def getList(cityName,num):
	outName=os.getcwd()+'/city.json'
	myOut=open(outName,'w')

	place=str(cityName).replace(' ','+')
	n=str(num)
	filehandle = urllib2.urlopen('http://dev.api.ean.com/ean-services/rs/hotel/v3/list?cid=55505&apiKey=rr6x8hf65zfdzkns9s4kxspz&minorRev=28&locale=en_US&currencyCode=USD&xml=%3CHotelListRequest%3E%0A%20%20%20%20%3Ccity%3E'+place+'%3C%2Fcity%3E%0A%20%20%20%20%3CcountryCode%3EIN%3C%2FcountryCode%3E%0A%20%20%20%20%3CarrivalDate%3E2%2F21%2F2015%3C%2FarrivalDate%3E%0A%20%20%20%20%3CdepartureDate%3E2%2F23%2F2015%3C%2FdepartureDate%3E%0A%20%20%20%20%3CnumberOfResults%3E'+n+'%3C%2FnumberOfResults%3E%0A%3C%2FHotelListRequest%3E')
	response=filehandle.read()
	data = json.loads(response)
	HotelList=data[u'HotelListResponse'][u'HotelList'][u'HotelSummary']
	Result={}
	for i in range(0,len(HotelList)):
		if u'tripAdvisorRating' in HotelList[i]:
			R={}
			R['name']= HotelList[i][u'name'].encode('ascii','ignore')
			R['tripAdvisorRating']=HotelList[i][u'tripAdvisorRating']
			R['hotelRating']=HotelList[i][u'hotelRating']
			Result[R['name']] = R
	json.dump(Result,myOut)