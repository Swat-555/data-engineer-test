import pandas as pd

# Load the dataset
df = pd.read_csv("tourism_dataset_local.csv")

# Group by 'country' and calculate average 'Rate'
grouped_df = df.groupby('country')['Rate'].mean().reset_index()
grouped_df.to_csv("SwatiShahi-test.csv", index=False)
print("Aggregated data saved to CSV.")

# SQL equivalent for grouping:
# SELECT country, AVG(Rate) FROM tourism_dataset GROUP BY country;

# Identify the top 3 categories with the highest average rate
top_categories = df.groupby('category')['Rate'].mean().nlargest(3).reset_index()
top_categories.to_csv("SwatiShahi-test-top3.csv", index=False)
print("Top 3 categories saved to CSV.")