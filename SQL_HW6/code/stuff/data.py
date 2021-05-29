from csv import reader
import re
import os
from collections import Counter

file_position = os.path.abspath(os.path.join(os.path.dirname(__file__),
                							'../stuff/access.log'))

PopularUrls_NUM = 10
Errors_NUM = 5

def read_data():
	with open(file_position) as file:
		data = reader(file, delimiter=' ')

		count = 0
		task1 = []
		task2 = []
		task3 = []
		task4 = []
		for i in data:
			count += 1
			task1.append(i[5].split(' ')[0]) # request type
			task2.append(i[5].split(' ')[1]) # urls
			if re.search('4[0-9]{2}', i[6]):
				task3.append([i[5].split(' ')[1], i[6], int(i[7]), i[0]])
			elif re.search('5[0-9]{2}', i[6]):
				task4.append(tuple([i[5].split(' ')[1], i[0]])) 

	res = list(zip(Counter(task1).keys(), Counter(task1).values()))
	res = sorted(res, key = lambda x: x[1], reverse=True)

	urls = list(zip(Counter(task2).keys(), Counter(task2).values()))
	urls = sorted(urls, key = lambda x: x[1], reverse=True)

	err4 = sorted(task3, key = lambda x: x[2], reverse=True)

	err5 = list(zip(Counter(task4).keys(), Counter(task4).values()))
	err5 = sorted(err5, key= lambda x: x[1], reverse=True)
	
	return [count, res, urls[0:PopularUrls_NUM], err4[0:Errors_NUM], err5[0:Errors_NUM]]
