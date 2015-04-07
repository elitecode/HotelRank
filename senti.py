from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import json, pickle, math

def compare(a,b):
	c = int(math.floor(a['rating']+a['tripAdvisorRating']*2 - b['rating']-b['tripAdvisorRating']*2))
	return c

def load_classifier():
	f = open('NB_classifier.pickle')
	classifier = pickle.load(f)
	f.close()
	return classifier

def sentimentAnalysis():
	fi = open("reviews.json")
	cityHotels = open("city.json")
	data = json.load(fi)
	hoteldata = json.load(cityHotels)
	count = 0
	hList = []
	for hotel in data:
		rcount = data[hotel]['count']
		reviews = data[hotel]['reviews']
		if data[hotel]['count'] >= 50:
			count+=1
			bin=[0,0,0,0,0,0,0,0,0,0]
			for rev in reviews:			
				blob = TextBlob(rev)
				pol =  blob.sentiment.polarity
				bin[int(math.ceil((pol+1)*5))-1]+=1
			rating = 0
			bsum = 0
			for i in range(10):
				rating += bin[i]*(i+1)
				bsum += bin[i]
			rating /= float(bsum)
			hoteldata[hotel]['rating'] = round(rating,2)
			hList.append(hoteldata[hotel])

	hList = sorted(hList,cmp=compare)

	fo = open("final.json","w")
	json.dump(hList,fo)
	cityHotels.close()
	fi.close()

def getSentimentRating():
	fi = open("reviews.json")
	data = json.load(fi)
	count = 0
	for hotel in data:
		rcount = data[hotel]['count']
		reviews = data[hotel]['reviews']
		if data[hotel]['count'] >= 50:
			count+=1
			bin=[0,0,0,0,0,0,0,0,0,0]
			for rev in reviews:			
				blob = TextBlob(rev)
				pol =  blob.sentiment.polarity
				bin[int(math.ceil((pol+1)*5))-1]+=1
			rating = 0
			bsum = 0
			for i in range(10):
				rating += bin[i]*(i+1)
				bsum += bin[i]
			rating /= float(bsum)
			rating = round(rating,2)
	fi.close()
	return rating

# hotel = hotel.encode('ascii','ignore')
# 		if hoteldata[hotel]['hotelRating'] == 1:
# 			star1.append(data[hotel])
# 		elif hoteldata[hotel]['hotelRating'] == 2:
# 			star2.append(data[hotel])
# 		elif hoteldata[hotel]['hotelRating'] == 3:
# 			star3.append(data[hotel])
# 		elif hoteldata[hotel]['hotelRating'] == 4:
# 			star4.append(data[hotel])
# 		elif hoteldata[hotel]['hotelRating'] == 5:
# 			star5.append(data[hotel])
		
# 		print star3

# text = 'This is a good hotel. had a lot of sex'
# t2 = 'the stay was excellent'
# blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())
# bl = TextBlob(t2)
# # print(blob.sentiment.analyze())
# # print(bl.sentiment.analyze())
# # PatternAnalyzer.analyze(blob)
# print blob.sentiment
# print bl.sentiment