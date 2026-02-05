import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

# a) Create synthetic dataset
# Features: [Packet Size, Duration]
X = np.array(
    [
        [200, 1],
        [220, 2],
        [250, 1],  # Normal
        [800, 5],
        [900, 6],
        [850, 7],  # Malicious
    ]
)

# Labels: Normal = 0, Malicious = 1
y = np.array([0, 0, 0, 1, 1, 1])

# b) Train KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# c) Predict and show confusion matrix
y_pred = knn.predict(X)
cm = confusion_matrix(y, y_pred)

print("Predictions:", y_pred)
print("Confusion Matrix:\n", cm)
