import csv
import random

import numpy as np


# a) Generate CSV file with employee metrics
def generate_csv():
    with open("employees.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["ID", "Metric1", "Metric2"])
        for i in range(100):
            m1 = random.randint(10, 100)
            m2 = random.randint(20, 120)
            w.writerow([i, m1, m2])
    print("employees.csv created.")


# b) Demonstrate f.tell() and f.seek()
def show_file_cursor():
    f = open("employees.csv", "r")

    print("Cursor at start:", f.tell())  # position 0
    print(f.readline())  # read first line
    print("Cursor after reading header:", f.tell())

    f.seek(0)  # reset cursor to beginning
    print("Cursor after seek(0):", f.tell())

    f.close()


# c) Load numeric columns into NumPy arrays and compute stats
def load_numpy_stats():
    metric1 = []
    metric2 = []

    with open("employees.csv") as f:
        r = csv.reader(f)
        next(r)  # skip header
        for _, m1, m2 in r:
            metric1.append(int(m1))
            metric2.append(int(m2))

    m1_arr = np.array(metric1)
    m2_arr = np.array(metric2)

    print(
        "Metric1 → Mean:", m1_arr.mean(), " Min:", m1_arr.min(), " Max:", m1_arr.max()
    )
    print(
        "Metric2 → Mean:", m2_arr.mean(), " Min:", m2_arr.min(), " Max:", m2_arr.max()
    )


# -------- MAIN EXECUTION --------
generate_csv()
show_file_cursor()
load_numpy_stats()
