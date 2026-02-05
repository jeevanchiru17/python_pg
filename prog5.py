import csv
import random

import matplotlib.pyplot as plt


# a) Generate students.csv with ID, Branch, Score
def generate_csv():
    with open("students.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Branch", "Score"])  # header
        for i in range(1000):
            branch = random.choice(["CS", "EE", "ME"])
            score = random.randint(0, 300)
            w.writerow([i, branch, score])
    print("students.csv created.")


# b) Load + classify into categories
def load_and_classify():
    data = []
    with open("students.csv") as f:
        r = csv.reader(f)
        next(r)  # skip header
        for id, branch, score in r:
            score = int(score)

            if score < 100:
                cat = "Fail"
            elif score < 200:
                cat = "Pass"
            elif score < 250:
                cat = "Good"
            else:
                cat = "Excellent"

            data.append([id, branch, score, cat])

    return data


# c) Plot Histogram for score distribution
def plot_hist(scores):
    plt.hist(scores, bins=20)
    plt.xlabel("Scores")
    plt.ylabel("Frequency")
    plt.title("Students Score Distribution")
    plt.show()


# -------- MAIN EXECUTION --------
generate_csv()
students = load_and_classify()

# Extract only Score column
scores = [s[2] for s in students]
plot_hist(scores)
