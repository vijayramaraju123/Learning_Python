

import re

# $ means end of the line
# [0-9]$

result = re.search(r'abc$','123abc')
print("Match!" if result else "No Match")

result = re.search(r'abc$','abc123')
print("Match!" if result else "No Match")

Class_46_04_RegularExpression.py


import re

# \d or [0-9]

# \d\d\d\d or \d{4}

#\D or [^0-9]  -> Single non digit
#\w or [a-zA-Z0-9] -> Any alphaneumeric
#\W or [^a-zA-Z0-9] -> Any non alphaneumeric


text = "Hello World\t Python\nRocks \rCoding \ffun"
result = re.findall(r'\s',text)
print(f"Matched white characters: {result}")
print(f"Number of whiltespaces matches :{len(result)}")


txt = "foo football food foo-bar bar foo"
mach = re.findall(r'\bfoo\b',txt)
print(mach)
