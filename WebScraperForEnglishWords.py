########## Web Scraper for words in the english dictionary ##########

import string
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def scraper():
	allRhymes = []
	rhymesPerPage = []
	base_url = "https://learnersdictionary.com/3000-words/alpha"

	for i in string.ascii_lowercase:
		query_parameter = "/" + str(i)

		for x in range(80):
			page_num = "/" + str(x)
			url = base_url + query_parameter + page_num
			response = requests.get(url)
			soup = bs(response.content, 'html.parser')
			wordClasses = soup.find_all("ul", attrs={"class", "a_words"})
			print(i, x, " ", wordClasses)
			for j in range(len(wordClasses)):
				rhymesPerPage.append(wordClasses[j].text)

	for k in range(len(rhymesPerPage)):
		allRhymes.append(rhymesPerPage[k])

	return allRhymes


words = scraper()

i = range(1, len(words) + 1)
words_data_frame = pd.DataFrame({'words': words}, index=i)

print(words_data_frame)

words_data_frame.to_csv('C:\\Users\\dd\\Desktop\\Words.txt', )
