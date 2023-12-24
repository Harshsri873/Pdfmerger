# Pdfmerger
import PyPDF2

print("rename your pdf as 1.pdf,2.pdf,3.pdf")
pdfiles = ["1.pdf","2.pdf","3.pdf"]
merger = PyPDF2.PdfMerger()
for pdf in pdfiles:
    pd1 = open(pdf,'rb')
    pdfreader = PyPDF2.PdfReader(pd1)
    merger.append(pdfreader)
pd1.close()
merger.write("merged.pdf")
print("Your merged pdf is ready with the name of merged.pdf")
