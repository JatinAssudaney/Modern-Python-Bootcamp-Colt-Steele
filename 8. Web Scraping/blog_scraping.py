# https://www.rithmschool.com/blog
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.rithmschool.com/blog"
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text,"html.parser")
articles = soup.find_all("article")
# print(articles)
with open("blog_data.csv","w") as file:
	csv_writer = writer(file)
	csv_writer.writerow(["title","url","date"])
	for article in articles:
		# print(article.find("a").get_text())
		title = article.find("a").get_text()
		links = article.find("a")['href']
		time = article.find("time")['datetime']
		csv_writer.writerow([title,links,time])