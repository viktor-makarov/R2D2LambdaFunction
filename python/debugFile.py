import countTokens;

event = {"text": "test text from AWS","model": "gpt-4o"}

result = countTokens.countTokenInTextRouter(event,"")

print("result",result)