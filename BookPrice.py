import urllib2
import requests
from bs4 import BeautifulSoup as BS

class BookPrice:
	def __init__(self):
		print("Welcome to DrEvans-'s Craiglist Parser!");
		print("I will be adding more functionality as I progress.");
		print("There may be some bugs, but don't fret, I am working on them!");
		self.promptInput()

	def promptInput(self):
		city = raw_input("Your city (all lowercase!): ");
		query = raw_input("Search your query: ")
		self.search(city, query)

	def search(self, city, query):
		site = "http://" + city + ".craigslist.org/search/bka/"
		payload = {"query": query}
		r = requests.get(site, params=payload)
		print("URL for your query: " + r.url + "\n")

		soup = BS(r.text)

		htmlList = soup.find(id="toc_rows").findAll("p", class_="row")

		self.displaySearchResults(htmlList)

		print ""
		self.promptInput()

	def displaySearchResults(self, htmlList):
		for item in htmlList:
			date = item.find("span", class_="pl").find("span", class_="date")
			if date != None:
				date = date.get_text()			
				print("Date: " + date)		
			else:
				print("Date: not listed")			

			title = item.span.a
			if title != None:
				title = title.get_text()			
				print("Title: " + title)	
			else:
				print("Title: not listed")

			price = item.find("span", class_="l2").find("span", class_="price")
			if price != None:
				price = price.get_text()			
				print("Price: " + price)		
			else:
				print("Price: not listed")

			place = item.find("span", class_="l2").find("span", class_="pnr").find("small")
			if place != None:
				place = place.get_text()			
				print("Place: " + place[2:-1])		
			else:
				print("Place: not listed")
			
			print "----------------------------"
			
BookPrice()
