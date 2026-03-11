
# Gene Expression Analysis and Visualization

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (handle encoding issues)
data = pd.read_csv("gene_expression.csv2", encoding="latin-1")

# Display data
print("Gene Expression Data:")
print(data)

# Basic statistics
average_expression = data["Expression_Level"].mean()
print("\nAverage Expression Level:", average_expression)

# Plot gene expression
plt.figure()
plt.bar(data["Gene"], data["Expression_Level"])
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.show()