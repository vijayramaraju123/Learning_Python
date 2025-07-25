import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep='\t')
print(chipo.head())
print(chipo.shape[0])
print(chipo.info())
print(chipo.shape[1])
print(chipo.columns)


print(chipo.index)
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

c = chipo.groupby('choice_description').sum()
c = c.sort_values(['quantity'], ascending=False)
print(c.head(1))

total_items_orders = chipo.quantity.sum()
print(total_items_orders)

print(chipo.item_price.dtype)

orders = chipo.order_id.value_counts().count()
print(orders)




chipo.item_name.value_counts().count()
