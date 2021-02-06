from utils import (
	doc_from_path,
	text_files_in_directory,
	load_nlp,
	words_for_doc,
	sentence_count,
	wordcount,
	)

def get_words(path):
	with open(path) as f:
		return [line.strip() for line in f.readlines()]

FAMILIAR_WORDS = set(get_words('resources/familiar-words.txt'))

# TODO: stemming
def difficult_word_rate(doc):
	words = words_for_doc(doc)
	difficult_words = [w for w in words if not w.lower() in FAMILIAR_WORDS]
	return len(difficult_words) / len(words)

def dc_grade_level(doc):
	word_rate_term = 0.1579 * difficult_word_rate(doc) * 100
	sentence_length_term = .0496 * wordcount(doc) / sentence_count(doc)
	return word_rate_term + sentence_length_term

import os

if __name__ == '__main__':
	from flesch_kincaid import (
		fk_grade_level,
		fk_readability,
	)
	
	nlp = load_nlp()
	dirpath = '/Users/jbrew/desktop/github/karaoke/sources/text/wikipedia'

	for path in text_files_in_directory(dirpath):
		doc = doc_from_path(path, nlp)
		print(path)
		print(f"\tfk grade level: {fk_grade_level(doc)}")
		print(f"\tfk readability: {fk_readability(doc)}")
		print(f"\tdc grade level: {dc_grade_level(doc)}")