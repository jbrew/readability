from utils import (
	avg_sentence_length_for_doc,
	doc_from_path,
	text_files_in_directory,
	load_nlp,
	words_for_doc,
	stem,
	)

def get_words(path):
	with open(path) as f:
		return [line.strip() for line in f.readlines()]

familiar_words = get_words('resources/familiar-words.txt')
FAMILIAR_WORDS = set(familiar_words)
FAMILIAR_STEMS = set([stem(w) for w in familiar_words])

def difficult_word_rate_for_doc(doc):
	words = words_for_doc(doc)
	difficult_words = [w for w in words if word_is_difficult(w)]
	return (len(difficult_words) / len(words)) * 100

def difficult_words_for_doc(doc):
	return [w for w in words_for_doc(doc) if word_is_difficult(w)]

def word_is_difficult(word, with_stemming=True):
	if with_stemming:
		return stem(word.lower()) not in FAMILIAR_STEMS
	return word not in FAMILIAR_WORDS

def dc_grade_level(doc):
	word_rate_term = 0.1579 * difficult_word_rate_for_doc(doc)
	sentence_length_term = 0.0496 * avg_sentence_length_for_doc(doc)
	adjustment = 3.6365 if word_rate_term > 0.05 else 0
	return word_rate_term + sentence_length_term + adjustment

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
		print(difficult_word_rate_for_doc(doc))
		print(avg_sentence_length_for_doc(doc))	