import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 18, 47],
    'Department': ['HR', 'Finance', 'IT', 'Marketing']
})

# Query: Find people older than 30
df.query('Age > 30')
# Employees in Finance older than 30
df.query("Department == 'Finance' and Age > 30")