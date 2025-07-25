

import pandas as pd

# Pandas are tow types
# Series and dataframes

s1 = pd.Series()
print(s1)



l1 = [1,2,3,4]
s2 = pd.Series(l1)
print(s2)
print(l1)


fruit_dict = {1:'apple',2:'mango',3:'banana'}
s3 = pd.Series(fruit_dict)
print(s3)



