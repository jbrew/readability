from utils import (
	avg_sentence_length_for_doc,
	words_for_doc,
	words_of_at_least_n_syllables_for_doc,
)

def percent_hard_words(doc):
	return 100 * len(words_of_at_least_n_syllables_for_doc(doc, 3)) / len(words_for_doc(doc))

def gf_grade_level(doc):
	return 0.4 * (avg_sentence_length_for_doc(doc) + percent_hard_words(doc))