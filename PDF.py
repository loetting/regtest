# # coding: utf-8

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import urllib2
import os

class PDF:

    def __init__(self, url):
        self.url = url
        self.destination = None

    # download PDF from source URL to local machine for processing
    # params: destination (file to save working PDF)
    def download(self, destination):
        source_file = urllib2.urlopen(self.url)
        data = source_file.read()
        with open(destination, mode='wb') as destination_file:
            destination_file.write(data)
        self.destination = destination

    # extract text from PDF
    # params: None
    def get_text(self):
        if not self.destination:
            # TODO better exception/error handling
            raise Exception('Must download file first, call pdf.download()')
        
        resource_manager = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(resource_manager, retstr, codec=codec, laparams=laparams)
        document = open(self.destination, 'rb')
        interpreter = PDFPageInterpreter(resource_manager, device)
        caching = True
        pagenos = set()
        for page in PDFPage.get_pages(document):
            interpreter.process_page(page)

        text = retstr.getvalue().decode('ascii', 'ignore')
        document.close()
        device.close()
        retstr.close()
        return text

    # remove local working copy of PDF
    # params: None
    def remove(self):
        os.remove(self.destination)
        self.destination = None
