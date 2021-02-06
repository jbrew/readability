import nltk
import os
import re
import spacy

cmu = nltk.corpus.cmudict.dict()
print(f"{len(cmu)} words in pronouncing dictionary")

def load_nlp():
	return spacy.load("en_core_web_sm")

def clean(word):
	word = word.lower()
	word = word.strip()
	word = word.replace('.','')
	word = word.replace(',','')
	return word

def words_for_sentence(sentence):
	words = re.findall(r"[\w']+", sentence)
	return [clean(word) for word in words if len(word) > 0]

def phones_for_word(word):
	prons = cmu.get(word.lower())
	return prons[0] if prons else []	# TODO: estimate syllables for unknown words

def all_vowels_for_phones(phones):
	return [phone for phone in phones if phone[-1] in '012']

def syllable_count_for_phones(phones):
	return len(all_vowels_for_phones(phones))

def syllable_count_for_word(word):
	return syllable_count_for_phones(phones_for_word(word))

def words_for_doc(doc):
	words = []
	for sent in list(doc.sents):
		words.extend(words_for_sentence(sent.text))
	return words

def syllable_count_for_doc(doc):
	words = words_for_doc(doc)
	return sum([syllable_count_for_word(word) for word in words])

def wordcount(doc):
	return len(words_for_doc(doc))

def syllable_count(doc):
	return sum([syllable_count_for_word(word) for word in words_for_doc(doc)])

def polysyllable_count(doc):
	polysyllables = [word for word in words_for_doc(doc) if syllable_count_for_word(word) >= 3]
	return len(polysyllables)

def sentence_count(doc):
	return len(list(doc.sents))

## LOADING TEXT

def text_from_path(path):
	with open(path) as f:
		return f.read()

def doc_from_path(path, nlp):
	return nlp(text_from_path(path))

def text_files_in_directory(dirpath):
	paths = [os.path.join(dirpath, fname) for fname in os.listdir(dirpath)]
	return [path for path in paths if path.endswith('.txt')]
