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

# Create barplot (512x512 px output)
plt.figure(figsize=(8, 8))  # 8x8 inches × 64 dpi = 512×512 px
sns.barplot(data=df, x="Category", y="Satisfaction", palette="viridis")

plt.title("Average Customer Satisfaction by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Avg. Satisfaction Score")
plt.xticks(rotation=20)

plt.tight_layout()

# Export PNG
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
