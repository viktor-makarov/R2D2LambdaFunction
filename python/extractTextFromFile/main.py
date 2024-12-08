import http.client
import urllib.parse
from io import BytesIO
import filetype
from docx import Document
import openpyxl
import PyPDF2

def download_file(url):
    # Parse the URL to extract components
    url_parts = urllib.parse.urlparse(url)
    conn = http.client.HTTPSConnection(url_parts.netloc)
    conn.request("GET", url_parts.path)
    response = conn.getresponse()
    
    if response.status != 200:
        raise Exception(f"Failed to download file: {url} {response.status} {response.reason}")
    
    # Read the response data into a BytesIO object
    return BytesIO(response.read())

def getmimetype(byte_stream):
    # Move to the beginning of the stream
    byte_stream.seek(0)
    # Use filetype to detect MIME type
    kind = filetype.guess(byte_stream.read(2048))  # Read the first 2048 bytes for better detection
    if kind is None:
        raise ValueError("Could not determine MIME type")
    return kind.mime

def extracttextfromtxt(txt_stream):
    return txt_stream.read().decode('utf-8')

def extracttextfromxlsx(xlsx_stream):
    wb = openpyxl.load_workbook(xlsx_stream, data_only=True)
    text = []
    for sheet in wb.sheetnames:
        ws = wb[sheet]
        for row in ws.iter_rows():
            text.append(' '.join([str(cell.value) if cell.value is not None else '' for cell in row]))
    return "\n".join(text)

def extracttextfromdocx(docx_stream):
    doc = Document(docx_stream)
    return "\n".join([paragraph.text for paragraph in doc.paragraphs])

def extracttextfrompdf(pdf_stream):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_stream)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extracttextfromfile(filestream, mime_type):
    text = ""
    
    if mime_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        print("doc")
        text = extracttextfromdocx(filestream)
    elif mime_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        print("Excel")
        text = extracttextfromxlsx(filestream)
    elif mime_type.startswith('text/'):        
        print("Text")
        text = extracttextfromtxt(filestream)
    elif mime_type == 'application/pdf':
        print("PDF")
        text = extracttextfrompdf(filestream)
    else:
        raise ValueError("Unsupported file type")
    
    return text

def extractTextFromFileRouter(event, context):
  
    url = event["url"]
    filestream = download_file(url)
    mime_type  = getmimetype(filestream)
    print("mimetype",mime_type)

    if mime_type is None:
        raise ValueError("Could not determine MIME type")
    
    text = extracttextfromfile(filestream, mime_type)

    return {
        'statusCode': 200,
        'body': {text:text}
    }