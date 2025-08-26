import re

txt="I have 2 apples, 15 oranges, and 100 grapes"

m= re.findall(r'[\d]', txt)

if m:
     print(m)
else:
     print('y')