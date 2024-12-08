import extractTextFromFile;

event = {"url": "https://r2d2storagedev.s3.eu-north-1.amazonaws.com/incoming_files/test_text2.txt"}

result = extractTextFromFile.extractTextFromFileRouter(event,"")

print("result",result)