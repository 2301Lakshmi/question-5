import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate synthetic data
np.random.seed(42)
categories = ["Electronics", "Home & Kitchen", "Fashion", "Sports", "Beauty"]
scores = np.random.normal(loc=[4.2, 4.0, 3.8, 4.1, 4.3], scale=0.2, size=5)

df = pd.DataFrame({"Category": categories, "Satisfaction": scores})

# Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create barplot (must be exactly 512x512 px)
plt.figure(figsize=(8, 8))  # 8 inches × 64 dpi = 512 pixels
sns.barplot(data=df, x="Category", y="Satisfaction", palette="viridis")

plt.title("Average Customer Satisfaction by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Avg. Satisfaction Score")
plt.xticks(rotation=20)

plt.tight_layout()

# Save EXACT 512x512 px image
plt.savefig("chart.png", dpi=64)   # IMPORTANT: no bbox_inches='tight'
plt.close()

