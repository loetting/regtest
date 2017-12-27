# #!/usr/bin/python
# # coding: utf-8

import sys
import time
from RegulationNLP import RestrictiveWordClassifier, RegDataNLP, Dandelion, RegulatoryHierarchyClassifier
from PDF import PDF

if len(sys.argv) != 2:
    print "Must include URL to regulatory pdf"
    sys.exit()

url = sys.argv[1]

# download and parse PDF into machine readable text
pdf = PDF(url)
pdf.download('working_download.pdf')
text = pdf.get_text()
pdf.remove()
print "-------------------------"

classifier = RegulatoryHierarchyClassifier(text)
sections = classifier.getSubsections()
print classifier.getDivision()['title']
for s in sections:
    print s['title']

# write machine readable text to file for review
filename = "results/pdf_to_text_%s.txt" % (time.time())
print "TEXT FILE: "
print filename
file = open(filename, 'w')
file.write(text)

# count number of restrictive words
classifier = RestrictiveWordClassifier()
print "RESTRICTIVE WORD COUNT:"
print classifier.getCount(text)
print "-------------------------"

# grab some possible tags using nltk
print "POSSIBLE KEYWORDS, NLTK"
nlp = RegDataNLP()
entities = nlp.getNamedEntities(text)
for entity in entities:
    print entity
print "-------------------------"

# grab some possible tags using tf-idf
print "POSSIBLE KEYWORDS, TF-IDF"
nlp = RegDataNLP()
keywords = nlp.getKeywords(text)
for keyword in keywords:
    print keyword
print "-------------------------"

# grab some possible tags using Dandelion API
print "POSSIBLE TOPICS, DANDELION API "
dandelion = Dandelion()
keywords = dandelion.getEntities(text)
for keyword in keywords:
    print keyword
print "-------------------------"


