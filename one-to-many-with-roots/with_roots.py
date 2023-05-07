# %%

from translate import Translator
import spacy
from spacy.matcher import Matcher
from spacy.util import filter_spans
from spacy import displacy


nlp_english = spacy.load('en_core_web_sm')
nlp_german = spacy.load("de_core_news_sm")
nlp_french = spacy.load("fr_core_news_sm")
nlp_dutch = spacy.load("nl_core_news_sm")
nlp_italian = spacy.load("it_core_news_sm")
nlp_portuguese = spacy.load("pt_core_news_sm")
nlp_spanish = spacy.load("es_core_news_sm")

to_translate = str(input("Enter text to translate: "))

pattern = [{'POS': 'VERB', 'OP': '?'}]


# %%
english_matcher = Matcher(nlp_english.vocab)
english_matcher.add("Verb phrase", [pattern])

doc_english = nlp_english(to_translate)
matches = english_matcher(doc_english)
spans = [doc_english[start:end] for _, start, end in matches]

print(to_translate)
for i in range(len(filter_spans(spans))):
    print(filter_spans(spans)[i].root.lemma_)


# %%
translator_german = Translator(to_lang="de")
en_to_de = translator_german.translate(to_translate)
doc_de = nlp_german(en_to_de)

german_matcher = Matcher(nlp_german.vocab)
german_matcher.add("Verb phrase", [pattern])
doc_german = nlp_german(en_to_de)
german_matches = german_matcher(doc_german)
german_spans = [doc_german[start:end] for _, start, end in german_matches]
print(en_to_de)
for i in range(len(filter_spans(german_spans))):
    print(filter_spans(german_spans)[i].root.lemma_)


# %%
translator_dutch = Translator(to_lang="nl")
en_to_nl = translator_dutch.translate(to_translate)
doc_de = nlp_dutch(en_to_nl)

dutch_matcher = Matcher(nlp_dutch.vocab)
dutch_matcher.add("Verb phrase", [pattern])
doc_dutch = nlp_dutch(en_to_nl)
dutch_matches = dutch_matcher(doc_dutch)
dutch_spans = [doc_dutch[start:end] for _, start, end in dutch_matches]
print(en_to_nl)
for i in range(len(filter_spans(dutch_spans))):
    print(filter_spans(dutch_spans)[i].root.lemma_)

# %%
translator_french = Translator(to_lang="fr")
en_to_fr = translator_french.translate(to_translate)
doc_fr = nlp_french(en_to_fr)

french_matcher = Matcher(nlp_french.vocab)
french_matcher.add("Verb phrase", [pattern])

doc_french = nlp_french(en_to_fr)
french_matches = french_matcher(doc_french)
french_spans = [doc_french[start:end] for _, start, end in french_matches]

print(en_to_fr)
for i in range(len(filter_spans(french_spans))):
    print(filter_spans(french_spans)[i].root.lemma_)


# %%
translator_italian = Translator(to_lang="it")
en_to_it = translator_italian.translate(to_translate)
doc_italian = nlp_italian(en_to_it)

italian_matcher = Matcher(nlp_italian.vocab)
italian_matcher.add("Verb phrase", [pattern])

italian_matches = italian_matcher(doc_italian)
italian_spans = [doc_italian[start:end] for _, start, end in italian_matches]
print(en_to_it)
for i in range(len(filter_spans(italian_spans))):
    print(filter_spans(italian_spans)[i].root.lemma_)


# %%
translator_portuguese = Translator(to_lang="pt")
en_to_pt = translator_portuguese.translate(to_translate)
doc_portuguese = nlp_portuguese(en_to_pt)

portuguese_matcher = Matcher(nlp_portuguese.vocab)
portuguese_matcher.add("Verb phrase", [pattern])

portuguese_matches = portuguese_matcher(doc_portuguese)
portuguese_spans = [doc_portuguese[start:end]
                    for _, start, end in portuguese_matches]
print(en_to_pt)
for i in range(len(filter_spans(portuguese_spans))):
    print(filter_spans(portuguese_spans)[i].root.lemma_)

# %%
translator_spanish = Translator(to_lang="es")
en_to_es = translator_spanish.translate(to_translate)
doc_spanish = nlp_spanish(en_to_es)

spanish_matcher = Matcher(nlp_spanish.vocab)
spanish_matcher.add("Verb phrase", [pattern])

spanish_matches = spanish_matcher(doc_spanish)
spanish_spans = [doc_spanish[start:end]
                 for _, start, end in spanish_matches]
print(en_to_es)
for i in range(len(filter_spans(spanish_spans))):
    print(filter_spans(spanish_spans)[i].root.lemma_)


