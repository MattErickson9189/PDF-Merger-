#Python 3 PDF combiner

import os, PyPDF2, sys


path = sys.argv[1]
pagesScanned = 0;

pdfFiles = []

for filename in os.listdir(path):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    pdfFileObj = open(os.path.join(path,filename), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    for pageNum in range (0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        pagesScanned = pagesScanned+1
        print(pagesScanned)

pdfOutput = open(os.path.join(path,'Merged.pdf'), 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()

print("PDFs successfully merged")