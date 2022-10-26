# pip install pypdf2
import PyPDF2
	
# criar o file object
pdfFileObj = open(R'C:\Users\Rodrigo\Documents\GitHub\python\365_DIAS_DE_ PYTHON.pdf', 'rb')
	
# criar o reader
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	
# imprimir o número de páginas
print(pdfReader.numPages)
	
# criar um page object
pageObj = pdfReader.getPage(0)
	
# extrair texto da página
print(pageObj.extractText())
	
# fechar o objeto (liberar o doc)
pdfFileObj.close()
