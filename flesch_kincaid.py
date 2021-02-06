from utils import (
	load_nlp,
	doc_from_path,
	text_files_in_directory,
	wordcount,
	syllable_count,
	sentence_count,
	)


## Flesch-Kincaid

def fk_grade_level(doc):
	"""
	Flesch-Kincaid grade level computed with this formula:
	https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
	"""

	num_words = wordcount(doc)
	num_sentences = sentence_count(doc)
	num_syllables = syllable_count(doc)

	return 0.39 * (num_words / num_sentences) + 11.8 * (num_syllables / num_words) - 15.59

def fk_readability(doc):
	num_words = wordcount(doc)
	num_sentences = sentence_count(doc)
	num_syllables = syllable_count(doc)

	sl = num_words / num_sentences
	nosw = num_syllables / num_words

	return 206.835 - 1.015 * sl - 84.6 * nosw

###

if __name__ == "__main__":
	dirpath = '/Users/jbrew/desktop/github/karaoke/sources/text/wikipedia'
	paths = text_files_in_directory(dirpath)

	nlp = load_nlp()
	for path in paths:
		print(path)
		doc = doc_from_path(path, nlp)
		print(fk_grade_level(doc))




