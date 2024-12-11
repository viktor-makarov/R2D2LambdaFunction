import extractTextFromFile;


#event = {"file_url":"https://r2d2storagedev.s3.eu-north-1.amazonaws.com/incoming_files/5248593849_1893.pdf","file_mime_type":"application/pdf"}

#event = {"file_url": "https://r2d2storagedev.s3.eu-north-1.amazonaws.com/incoming_files/5248593849_1866.txt", "file_mime_type": "text/plain"}

event = {"file_url":"https://r2d2storagedev.s3.eu-north-1.amazonaws.com/incoming_files/5248593849_1901.xlsx","file_mime_type":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"}


#event = {"file_url": "https://r2d2storagedev.s3.eu-north-1.amazonaws.com/incoming_files/5248593849_1867.json", "file_mime_type": "application/json"}

#event = {"file_url":"https://r2d2storagedev.s3.eu-north-1.amazonaws.com/incoming_files/5248593849_1875.docx","file_mime_type":"application/vnd.openxmlformats-officedocument.wordprocessingml.document"}

result = extractTextFromFile.extractTextFromFileRouter(event,"")

print("result",result)