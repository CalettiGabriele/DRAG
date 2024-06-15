# DRAG

DRAG is a data analysis tool. It speeds up the writing of code through the use of Large Language Models (LLMs), and is designed to be used the most popular format in the data analysis business, i.e. python notebooks (ipynb).
DRAG is an advanced RAG system specially designed to work with structured data in Pandas dataframes and return answers in Python code.

```python
from drag import ask
ask({"df": df}, "Shows the trend in house prices as area increases")
```

```python
import matplotlib.pyplot as plt

# Group the data by Superficie (m²) and calculate the mean of Prezzo (EUR)
grouped_df = df.groupby('Superficie (m²)')['Prezzo (EUR)'].mean().reset_index()

# Create a scatter plot of the data
plt.figure(figsize=(10, 6))
plt.scatter(grouped_df['Superficie (m²)'], grouped_df['Prezzo (EUR)'])
plt.xlabel('Superficie (m²)')
plt.ylabel('Prezzo (EUR)')
plt.title('Relationship between Surface Area and Price')
plt.show()
```