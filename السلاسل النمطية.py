import re

adress = """"my address 123.564.766 133

Ali adress 165.735.543 154
mohammed adress 134.567.763 188"""

regexer=re.split(r'\n+',adress)
print(regexer)