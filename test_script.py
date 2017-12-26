# #!/usr/bin/python
# # coding: utf-8

from RegulationNLP import RestrictiveWordClassifier, RegDataNLP, Dandelion
from PDF import PDF

url = 'https://www.sos.mo.gov/cmsimages/adrules/csr/current/2csr/2c30-10.pdf'
pdf = PDF(url)
pdf.download('testing_download.pdf')
text = pdf.get_text()
pdf.remove()

classifier = RestrictiveWordClassifier()
print "COUNT:"
print classifier.getCount(text)

nlp = RegDataNLP()
entities = nlp.getKeywords(text)
for entity in entities:
    print entity

# print "TEXT LENGTH: " + str(len(text))

# print "DANDELION: "
# dandelion = Dandelion()
# keywords = dandelion.getEntities(text)
