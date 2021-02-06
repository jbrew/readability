import os

from dale_chall import dc_grade_level
from flesch_kincaid import (
	fk_grade_level,
	fk_readability,
)
from smog import smog_grade_level
from utils import (
	load_nlp,
	text_files_in_directory,
	doc_from_path,
)


nlp = load_nlp()
dirpath = '/Users/jbrew/desktop/github/karaoke/sources/text/wikipedia'

for path in text_files_in_directory(dirpath):
	doc = doc_from_path(path, nlp)
	print(path)
	print(f"\tfk grade level: {fk_grade_level(doc)}")
	print(f"\tfk readability: {fk_readability(doc)}")
	print(f"\tdc grade level: {dc_grade_level(doc)}")
	print(f"\tsmog grade level: {smog_grade_level(doc)}")