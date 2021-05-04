#!/usr/bin/python3
from csv import reader
import re
from collections import Counter
import jsonpickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--json', action='store_true')
arg = parser.parse_args()


def read_data():
	with open("access.log") as file:
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
	
	return count, res, urls, err4, err5


def write_to_file(count, res, urls, err4, err5):
	with open('res.txt', 'w') as f:
		f.write(f'All requests: {count}\n\n')

		f.write('Types of request:\n')

		for i in res:
			f.write(f'{i[0]} - {i[1]}; ')
		f.write('\n\n')

		f.write('Most popular requests:\n')
		for i in urls[0:10]:
			f.write(str(i[0]) + ' - ')
			f.write(str(i[1]) + '\n')
		f.write('\n')

		f.write('Most heavy requests with 4xx:\n')
		for i in err4[0:5]:
			f.write(str(i[0]) + ' - ')
			f.write(str(i[1]) + ' - ')
			f.write(str(i[2]) + ' - ')
			f.write(str(i[3]) + '\n')
		f.write('\n')

		f.write('Top users whose requests(unique urls) - 5xx:\n')
		for i in err5[0:5]:
			f.write(str(i[0][1]) + ' - ')
			f.write(str(i[1]) + '\n')


def jsonify(count, res, urls, err4, err5):
	with open('results.json', 'w') as f:
		data1 = jsonpickle.encode(count)
		f.write(data1)
		f.write('\n')

		data2 = jsonpickle.encode(res)
		f.write(data2)
		f.write('\n')

		data3 = jsonpickle.encode(urls[0:10])
		f.write(data3)
		f.write('\n')

		data4 = jsonpickle.encode(err4[0:5])
		f.write(data4)
		f.write('\n')

		data5 = jsonpickle.encode([(a[0][1], a[1]) for a in err5[0:5]])
		f.write(data5)


count, res, urls, err4, err5 = read_data()
write_to_file(count, res, urls, err4, err5)

if arg.json:
	jsonify(count, res, urls, err4, err5)
	
