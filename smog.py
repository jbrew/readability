import math

from utils import (
	load_nlp,
	doc_from_path,
	text_files_in_directory,
	wordcount,
	sentence_count,
	polysyllable_count,
	)

def smog_grade_level(doc):
	"""https://en.wikipedia.org/wiki/SMOG"""
	root_term = polysyllable_count(doc) * 30 / sentence_count(doc)
	return 1.0430 * math.sqrt(root_term) + 3.1291

if __name__ == "__main__":
	pass