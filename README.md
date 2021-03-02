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

# Mental Age/Infantilization Annotated Bib

## Brashier, R. (2018). Incapacity and the Infancy Illation. Arkansas Law Review, 71 (1). 
- Primarily focused on older adults and issues of guardianship and conservatorship
- Section III: Why We Infantalize Adults with a Cognitive Impairment
  - Altruism – “pity” narrative; assumption of “knowing better” and genuinely wanting to take care
  - Assumptions – assuming our own acts are free of bias; assuming the line between able and disabled is stark and unmoving; Assuming “We Know What They Need”;   Assuming “We know how to protect them from themselves and others”; Assuming “That we know what they would have wanted had they not become incapacitated; Assuming “We should discount the wishes and preferences they now assert” 
  - Convenience: General convenience; Emotional convenience – facilitated autonomy/decision-making is time and labor intensive; Financial convenience 
  - Ignorance 
  - Self-Interest
- Conflation can be harmful 
- Ask:What do you want? Why do you want that? 

## Monteleone, 2017 (Eugenic Rubicon) 
- "In the early 20th century, diagnostic criteria for institutionalization and sterilization was often communicated through assigning the patient a mental age – if the age seemed incompatible with the ability to live independently or parent a future child, sterilization could mitigate future risks. The link between ‘mental age’ and paternalistic treatment seemed natural; how was a woman with the ‘mind of a child’ expected to live a productive life without supervision? French psychologists Alfred Binet and Theodore Simon developed the concept of ‘mental age’ in an effort to interpret newly designed intelligence testing. These tests first entered the United States in 1908 and saw widespread use categorizing incoming soldiers during World War I, leading to the controversial revelation that the average recruit had the ‘mental age’ of a young teenager (Carson, 2004). Even as the scandal of “feeble-minded” soldiers blazed across headlines, the use of mental age received robust contemporaneous critique. One 1922 article excoriates people who perpetuate this claim by stating that “the average adult intelligence cannot be less than  the average adult intelligence, and to anyone who knows what the words “mental age” mean Mr. Stoddard’s [contemporaneous author making 13-year old mental age claim] remark is precisely as silly as if he had written that the average mile was three quarters of a mile long.” (Lippman, 1922).  Mental age, however, remains a powerful narrative when discussing cognitive disability. Equating adults with cognitive disabilities to children continues to serve as justifications for infantilizing and paternalistic behaviors toward people with intellectual disabilities – including sterilization."
- “Having her size be more appropriate to her developmental level will make her less of a “freak”…there is nothing repulsive about a 2 month old infant, despite its limited cognitive, motor, and social skills. But when the 2 month old baby is put into a 20 year old body, the disconnect is jarring.” (Fost, 2007) 
These words, published in Scientific American in 2007, refer to a child named Ashley – known to the public only as Ashley X – who at the age of six underwent a full hysterectomy, mastectomy, and estrogen hormone treatment. The procedure was later deemed illegal because Ashley’s parents and doctors did not have a court order authorizing Ashley’s sterilization. Justifications for the Ashley Treatment often revolve evoke her “mental age” as justification, as exemplified by the above quote. This narrative infantilizes adults, justifies sterilization and social asexualization, and reinforces paternalistic attitudes and practices, despite the United Nations’ declaration of compulsory sterilization of people with disabilities “a form of violence and torture” 
  - Carson, J. (2004). The Science of Merit and the Merit of Science: Mental Order and Social Order in Early 20th Century United States and France in Jasanoff (Ed) States of Knowledge: The Co-Production of Science and Social Order. NJ: Routledge.
  - Fost, N. (2007, January 5). in Mims, C. The Pillow angel case – Three bioethicists weigh in. Scientific American.
  - Lippmann, W. (October 25 1922). The mental age of americans. The New Republic.
  - World Health Organization. (2014). Eliminating Forced, Coercive, and Otherwise Involuntary Sterilization: An Interagency Statement. Geneva, Switzerland: WHO, p. 5

## Stevenson, J., Harp, B., Gernsbacher, M. (2011). Infantilizing Autism. Disability Studies Quarterly. https://dsq-sds.org/article/view/1675/1596/. 
- “The stereotype of the "eternal child" has burned a disturbing path through history and continues to wreak havoc in arenas ranging from employment discrimination to forced sterilizations (Osburn, 2009; Pfeiffer, 1994; Wolfensberger, 1972).”
- NOTE: other citations are related to social role valorisation and normalisation theories (look at Wolfensberger book for more) 

## Robey, K., Beckley, L., and Kirschner, M. (2006). Implicit Infantilizing Attitudes about Disability. Journal of Developmental and Physical Disabilities, 18 (4), 441-453. 
- Abstract: This study serves as a preliminary investigation of implicit (unconscious) attitudes that associate disability with child-like features. A version of the Implicit Association Test was developed to assess the implicit association of disability-related words with words related to childhood. In order to assess its psychometric properties, this “infantilization IAT” was administered, along with a more evaluative IAT and measures of more explicit attitudes, two times over the course of three to five days to 30 staff persons of a facility that serves persons with multiple disabilities. The study's results: (1) Support the notion that individuals tend to implicitly associate disability-related words with words connoting childhood or child-like features; (2) Suggest that the infantilization IAT assesses attitudes that might not be captured through more traditional measurement strategies, and (3) Demonstrate divergent validity of the infantilization IAT when compared to results of the evaluative IAT, but (4) Also suggest relatively low test-retest reliability of the infantilization IAT

## Safia-Zecharia, L. (2018). The Infantilization of Intellectual Disability and Political Inclusion: A Pedagogical Approach. Journal of Educational Sciences, 19 (2), 104-112. 
- Abstract: The present paper looks at the way in which political and scientific frameworks, as well as everyday life dynamics work to exclude people living with intellectual disability (ID) in Romania from political life and how these dynamics could be overcome through crafting communicative-dialogic pedagogical interventions geared at political inclusion. I argue that the political exclusion of people with ID is built into the formal political order, as well as doubled by a twofold infantilizing dynamic. On the one hand, the scientific and academic psycho-pedagogical discourse still operates with classifications that inscribe people with ID with chronological "normal" ages inferior to their biological age. Their subject position is thus "fixed" at an age below the voting limited. This move is seconded by the way in which (formerly) institutionalized people with ID are referred to as "children" (despite their fully adult ages) in a small (post)institutional town, as well as in other care settings that I have explored ethnographically. Finally, the paper explores the stepping stones of alternative interventions, built on a communicative-dialogic methodology for politically including people with ID that could work to overcome the infantilizing dynamics.

## Smith, I. (2017). Mental Age Theory Hurts People with Intellectual Disabilities [Opinion]. NOS Magazine. 
- NOTE: Perspective of person with ID
- “Mental age theory discourages parents from teaching their disabled offspring their rights to independence and autonomy. A lot of my friends with intellectual disabilities have been mislead by mental age theory. They  feel they will never gain independence or get married because they have been told they are children and treated like children for their entire lives. This is why I advocate for people to not use mental age theory at all”
- “Educate people that it is not accurate or appropriate to refer someone with intellectual and developmental disabilities as mentally younger then they are! I not mentally 12. I am mentally 28. I just have an intellectual disability.”

## Gardiner, F. (2018). Parents, Do Not Infantilise Your Teenage and Adult Disabled Children. http://expectedly.org/blog/2018/06/parents-do-not-infantilise-your-teenage-and-adult-disabled-children/
- NOTE: Perspective of person with ID
- “If you’re a parent of a teenage or adult child with a disability, it’s important to avoid infantilising them. What is infantilisation? It’s treating people who are no longer children like children in a way that restricts their ability to be fully integrated with their age-peers. It’s talking to them in a condescending voice, dismissing their ideas and opinions, acting as though you will always understand them better than they understand themselves, or going out of your way to shield them from everything you think may be even slightly dangerous. It’s treating your child as though they will always be a child, no matter whether they’re 5, 15 or 35. Infantilisation is different from recognising that disabled people have support needs. That’s part of what being disabled means: being at a relative disadvantage compared to non-disabled people because we require specific supports to help us live within the community, whether that disadvantage is related to physical health, cognition, mental health, sensory processing or perception, mobility, or something else people find disabling.”
