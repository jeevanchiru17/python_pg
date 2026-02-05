import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# a) Synthetic movie review dataset
positive_words = ["amazing", "great", "loved", "fantastic", "super"]
negative_words = ["worst", "boring", "bad", "terrible", "poor"]

reviews = []
scores = []  # treated as "salary" values, per question

# Positive reviews → high salary
for i in range(50):
    reviews.append(positive_words[i % 5])
    scores.append(np.random.randint(60, 100))

# Negative reviews → low salary
for i in range(50):
    reviews.append(negative_words[i % 5])
    scores.append(np.random.randint(10, 50))

# Convert keywords to numeric (Positive=1, Negative=0)
X = np.array([[1] if r in positive_words else [0] for r in reviews])
y = np.array(scores)

# b) Train-test split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# c) Train Linear Regression model
model = LinearRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

# d) R² Score and RMSE
print("R² Score:", r2_score(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred) ** 0.5)

# Plot regression line
plt.scatter(X, y, color="blue", label="Actual Scores")
plt.plot(X, model.predict(X), color="red", label="Regression Line")

plt.xlabel("Review (1 = Positive, 0 = Negative)")
plt.ylabel("Salary/Score")
plt.title("Linear Regression on Movie Reviews")
plt.legend()
plt.show()
