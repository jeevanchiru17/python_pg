import csv
import random

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# a) Generate repository dataset with 3 profiles
def generate_repo_csv():
    with open("repos.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Stars", "Forks", "Commits"])

        # Viral repositories (high stars, medium forks, low commits)
        for _ in range(50):
            w.writerow(
                [
                    random.randint(5000, 10000),
                    random.randint(200, 500),
                    random.randint(50, 200),
                ]
            )

        # Active repositories (medium everything)
        for _ in range(50):
            w.writerow(
                [
                    random.randint(500, 2000),
                    random.randint(100, 300),
                    random.randint(400, 1500),
                ]
            )

        # Dead repositories (very low everything)
        for _ in range(50):
            w.writerow(
                [random.randint(0, 50), random.randint(0, 20), random.randint(0, 40)]
            )

    print("repos.csv generated.")


# Load CSV into tuple list
def load_as_tuples():
    data = []
    with open("repos.csv") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            stars, forks, commits = map(int, row)
            data.append((stars, forks, commits))
    return data


# -------- MAIN EXECUTION --------
generate_repo_csv()
data = load_as_tuples()

# Convert tuple list into list of lists for sklearn
X = [list(t) for t in data]

# b) Apply K-Means clustering (k=3)
kmeans = KMeans(n_clusters=3)
labels = kmeans.fit_predict(X)

# c) Scatter Plot (Stars vs Forks)
stars = [x[0] for x in X]
forks = [x[1] for x in X]

plt.scatter(stars, forks, c=labels)
plt.xlabel("Stars")
plt.ylabel("Forks")
plt.title("Repository Clustering (K = 3)")
plt.show()
