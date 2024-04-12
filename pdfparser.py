import requests
import io
import PyPDF2

def extract_text_from_pdf_url(url):
    # Send HTTP request to get the PDF
    response = requests.get(url)
    
    # Ensure the request was successful
    if response.status_code == 200:
        # Get the PDF content as a blob
        pdf_blob = response.content
        
        # Convert the blob into a file-like object
        pdf_file = io.BytesIO(pdf_blob)
        
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        # Iterate through each page and extract text
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            print(page.extract_text())
    else:
        print("Failed to retrieve PDF: Status code", response.status_code)

# Example usage
pdf_url = 'http://example.com/path_to_pdf.pdf'
extract_text_from_pdf_url(pdf_url)