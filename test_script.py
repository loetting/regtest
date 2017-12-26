# #!/usr/bin/python
# # coding: utf-8

from RestrictiveWordClassifier import RestrictiveWordClassifier
from PDF import PDF

url = 'https://www.sos.mo.gov/cmsimages/adrules/csr/current/2csr/2c30-10.pdf'
pdf = PDF(url)
pdf.download('testing_download.pdf')
text = pdf.get_text()
pdf.remove()

classifier = RestrictiveWordClassifier()
print "COUNT:"
print classifier.getCount(text)
