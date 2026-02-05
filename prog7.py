import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
from PIL import Image, ImageDraw

# a) Generate synthetic shopping transactions
transactions = [
    ["milk", "bread", "butter"],
    ["bread", "egg"],
    ["milk", "egg"],
    ["milk", "bread"],
    ["bread", "butter"],
    ["butter", "egg"],
    ["milk", "bread", "egg"],
    ["bread"],
    ["milk", "butter"],
]

# Convert to one-hot encoded dataframe
te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_data, columns=te.columns_)

# b) Apply Apriori algorithm (min support = 0.1)
freq_items = apriori(df, min_support=0.1, use_colnames=True)

# c) Generate association rules with lift > 1.0
rules = association_rules(freq_items, metric="lift", min_threshold=1.0)
top5 = rules.head(5)

print("Top 5 Rules:")
print(top5)

# d) Create a summary image of top 5 rules
img = Image.new("RGB", (600, 300), "white")
draw = ImageDraw.Draw(img)

y = 10
draw.text((10, y), "Top 5 Association Rules:", fill="black")
y += 30

for i, row in top5.iterrows():
    rule_text = f"{list(row['antecedents'])} -> {list(row['consequents'])} (lift={row['lift']:.2f})"
    draw.text((10, y), rule_text, fill="black")
    y += 25

img.save("rules_summary.png")
print("Image saved as rules_summary.png")
