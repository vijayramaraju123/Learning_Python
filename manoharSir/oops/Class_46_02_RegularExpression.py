



#^ start of the line
# ^[abc] means starts with a or b or c
# ^[^abc] starts other than a or b or c

import re

regex = r'Mahesh'
s='''pawas in good girl \n
Mahesh is aweeeesome \n
pawan is almighty'''

matches = re.findall(regex,s)
print(matches)
