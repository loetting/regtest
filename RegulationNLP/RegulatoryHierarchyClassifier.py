import re

class RegulatoryHierarchyClassifier:

    division_pattern = "Division ([0-9]+)\s*(.*)\n"
    chapter_pattern = "Chapter ([0-9]+)\s*(.*)\n"
    contents_pattern = "CSR %s-%s.([0-9]+)\s*([^\.]*)\.\.\.+"
    subsection_pattern = "Title\s+\d+[\d\D]+Division %s[\d\D]+Chapter %s[\d\D]+CSR\s+%s-%s([\d\D]+)(PURPOSE:[\d\D]+)\n\nAUTHORITY"

    def __init__(self, text):
        self.text = text
        self.subsections = []

        results = re.search(self.division_pattern, text)
        self.division = results.group(1)
        self.division_obj = {'number':results.group(1), 'title':results.group(2)}

        results = re.search(self.chapter_pattern, text)
        self.chapter = results.group(1)
        self.chapter_obj = {'number':results.group(1), 'title':results.group(2)}

        contents_pattern = self.contents_pattern % (self.division, self.chapter)
        results = re.findall(contents_pattern, text)
        for res in results:
            subsection = "%s.%s" % (self.chapter, res[0])
            self.subsections.append({'division':self.division, 'subsection':subsection, 'title':res[1].strip()})

        for curr_sub in self.subsections:
            pattern = self.subsection_pattern % (self.division, self.chapter, self.division, curr_sub['subsection'])
            results = re.search(pattern, text)
            curr_sub['text'] = results.group(2)

    # get array of subsections
    # params: None
    def getSubsections(self):
        return self.subsections

    # get division object (keys: title, number)
    # params: None
    def getDivision(self):
        return self.division_obj

    # get chapter object (keys: title, number)
    # params: None
    def getChapter(self):
        return self.chapter_obj
            

