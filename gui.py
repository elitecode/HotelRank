import Tkinter, json, os
import tkMessageBox
from hotelList import getList
from senti import sentimentAnalysis, getSentimentRating
top = Tkinter.Tk()

L1 = Tkinter.Label(top, text="City Name")
L1.pack()
E1 = Tkinter.Entry(top, bd =5)
E1.pack()

L2 = Tkinter.Label(top, text="Number of Hotels")
L2.pack()
E2 = Tkinter.Entry(top, bd =5)
E2.pack()

def rankHotels():
	cityName=E1.get()
	numOfHotels=E2.get()   
	getList(cityName,numOfHotels)
	os.system("scrapy crawl tripadvisor -s DOWNLOAD_DELAY=0.5")
	os.system("scrapy crawl tripadvisorreviews")
	sentimentAnalysis()
	os.system("python displayResults.py")	

B1 = Tkinter.Button(top, text ="Go", command = rankHotels)
B1.pack()

L3 = Tkinter.Label(top, text="Enter Name of Hotel")
L3.pack()
E3 = Tkinter.Entry(top, bd =5)
E3.pack()
def getSentiment():
	hotelName = E3.get()
	R={}
	R['name']= hotelName
	myOut = open("city.json","w")
	city = {}
	city[R['name']] = R
	json.dump(city,myOut)
	myOut.close()
	os.system("scrapy crawl tripadvisor")
	os.system("scrapy crawl tripadvisorreviews")
	rating = getSentimentRating()
	tkMessageBox.showinfo("Result","Rating: "+str(rating))

B2 = Tkinter.Button(top, text ="Get Rating", command = getSentiment)
B2.pack()


top.mainloop()