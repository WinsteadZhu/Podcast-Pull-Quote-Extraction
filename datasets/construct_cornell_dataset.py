import os
from collections import defaultdict
import re


def write_pq_to_file(i_url, url_str, all_sentences, edited_pq_texts, source_pq_texts, save_dir, movie_name):

	lines = []
	lines.append("{}\n{}".format(url_str, i_url))

	for edited, source in zip(edited_pq_texts, source_pq_texts):
		lines.append("\n----\n")
		lines.append("E: "+edited)

		lines.append("\n")
		lines.append("S: "+source)

	lines.append("\n========\n")
	for s in all_sentences:
		lines.append(s)


	# make sure we have a unique filename
	filename = save_dir + movie_name + '.txt'


	with open(filename, "w") as f:
		for l in lines:
			f.write(l+"\n")

	print("saved to file:", filename)

	return


all_movies = defaultdict(lambda: defaultdict(list))

scrip_f = open("./cornell_movie_quotes_data/moviequotes.scripts.txt", "r", encoding="ISO-8859-1")
scripts = scrip_f.readlines()

all_lines = {}

for line in scripts:
	idx_1, movie_name, idx_2, character, _, script = line.split(' +++$+++ ')
	movie_name = movie_name.replace(" ", "-")
	movie_name = movie_name.replace("/", "-")

	all_lines[idx_1] = script.strip()
	all_movies[movie_name]['all_sentences'].append(all_lines[idx_1])


quote_f = open("./cornell_movie_quotes_data/moviequotes.memorable_quotes.txt", "r", encoding="ISO-8859-1")
quotes = quote_f.read()

for block in quotes.split('\n\n'):
	block = block.strip()
	movie_name, edit, source, = block.split('\n')

	index, source = source.split(' ', 1)
	if index not in all_lines:
		print(index, source)
		print("MISSING in script")
		continue
	if source != all_lines[index]:
		print(index, source)
		print(all_lines[index])
		print("MISMATCH in script")
		continue

	movie_name = movie_name.replace(" ", "-")
	movie_name = movie_name.replace("/", "-")
	edit = edit.strip()
	source = source.strip()

	all_movies[movie_name]['edited_pq_texts'].append(edit)
	all_movies[movie_name]['source_pq_texts'].append(source)


save_dir = '../corpora/cornell-movie/'
i_url = '0'

for movie_name in all_movies:
	url_str = 'https://www.cornellmovie.com/' + movie_name
	all_sentences =  all_movies[movie_name]['all_sentences']
	edited_pq_texts = all_movies[movie_name]['edited_pq_texts']
	source_pq_texts = all_movies[movie_name]['source_pq_texts']
	if len(edited_pq_texts) > 0 and len(edited_pq_texts) == len(source_pq_texts):
		write_pq_to_file(i_url, url_str, all_sentences, edited_pq_texts, source_pq_texts, save_dir, movie_name)