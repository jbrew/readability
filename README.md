# Implementations of readability measures

1. Implementations of classic readability formulas
- [Flesch-Kincaid](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests)
- [Dale-Chall](https://en.wikipedia.org/wiki/Dale%E2%80%93Chall_readability_formula)
- [Gunning-Fog](https://en.wikipedia.org/wiki/Gunning_fog_index)
- [SMOG](https://en.wikipedia.org/wiki/SMOG) ("Simple Measure Of Gobbledegook")

2. Using BERT to (badly) simulate measures that actually depend on empirical results:
- BERT for [cloze testing](https://en.wikipedia.org/wiki/Cloze_test) in this [Colab notebook](https://colab.research.google.com/drive/1jnO57doC-dXfJQT2Aj8HgVfLEAbFlkzS#scrollTo=RIegRz7RM0M6)

# References

*Data-Driven Sentence Simplification: Survey And Benchmark*
https://www.mitpressjournals.org/doi/full/10.1162/coli_a_00370

*Supervised and Unsupervised Neural Approaches To Text Readability*
https://arxiv.org/pdf/1907.11779.pdf
- Comprehensive review of previous methods and datasets

*On Understanding the Relation between Expert Annotations of Text
Readability and Target Reader Comprehension*
https://www.aclweb.org/anthology/W19-4437.pdf
- "Computational models for automatic readability assessment (ARA) and automatic text simplification (ATS) ... are typically trained on corpora written by teachers or other experts, without a direct input from target readers.""

*Writing for Language-Impaired Readers*

*Supporting the Adaptation of Texts for Poor Literacy Readers: a Text Simplification Editor for Brazilian Portuguese (2009)*
https://www.aclweb.org/anthology/W09-2105.pdf
- "Reading comprehension entails three elements:the reader who is meant to comprehend; the text that is to be comprehended and the activity in which comprehension is a part of (Snow, 2002).  In addition to the content presented in the text, the vocabulary load of the text and its linguistic structure, discourse style, and genre interact with the reader’s knowledge"
- Study of syntactic simplification for Brazilian Portuguese
- On-line authoring tool for creating simplified texts: Simplifica (https://www.aclweb.org/anthology/N10-2011.pdf)

*Reporting simply*
https://www.w3.org/WAI/RD/2012/easy-to-read/paper7/
- Part of the *Simplext project* - Automatic text simplification system for Spanish for making newspaper articles more accessible to readers with cognitive disabilities.
- Not as many options in Spanish as with English because fewer large corpora are available.
- "Automatic lexical simplification is mainly seen as a task of synonym substitution"

*Practical simplification of english newspaper text to assist aphasic
readers*

*OneStopEnglish corpus*
https://www.aclweb.org/anthology/W18-0535.pdf
- Most contemporary approaches rely on large corpora from the web

*On the Applicability of Readability Models to Web Texts*
https://www.aclweb.org/anthology/C10-2032.pdf
- WeeBit corpus = WeeklyReader + BBCBiteSize

*Characterizing Text Difficulty With Word Frequencies*
https://www.aclweb.org/anthology/W16-0509.pdf
- SUBTLEX corpus: records film subtitles
"the amount of exposure of a reader to the word is believed to be the major predictor of word knowledge" (Ryder and Slater, 1988)

*A Comparison of Features for Automatic Readability Assessment*
https://www.aclweb.org/anthology/C10-2032.pdf
- Assigning text to elementary school grade levels
- Corpus is text labeled with grade levels 2-5. ** What corpus would be better than this for audience-specific readability? ** 

This paper reports POS analysis as among the strongest

"While pre-processing the texts, we found that many articles, especially those for lower grade levels, consist of only puzzles and quizzes, often in the form of simple multiple-choice questions. We discarded such texts"

Shallow Features:
average number of syllables per word
percentage of poly-syll. words per doc.
average number of poly-syll. words per sent.
average number of characters per word
Chall-Dale difficult words rate per doc.
average number of words per sentence
Flesch-Kincaid score
total number of words per document