

import re

# $ means end of the line
# [0-9]$

result = re.search(r'abc$','123abc')
print("Match!" if result else "No Match")

result = re.search(r'abc$','abc123')
print("Match!" if result else "No Match")
