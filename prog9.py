import csv
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


# a) Generate synthetic faculty dataset (1000 rows)
def generate_faculty_csv():
    with open("faculty.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "Experience",
                "Designation",
                "Salary",
                "Publications",
                "BookChapters",
                "Consultancy",
                "Funds",
                "Membership",
                "TextData",
            ]
        )

        for exp in range(1, 1001):
            # Linear mappings
            designation = (
                "Professor" if exp > 15 else "Associate" if exp > 7 else "Assistant"
            )
            salary = 30000 + exp * 2000
            publications = exp * 1
            book_ch = exp // 2
            consultancy = exp * 5000
            funds = exp * 10000
            membership = exp // 3

            # Random text for classification
            text = random.choice(
                [
                    "excellent teacher and researcher",
                    "good academic contributor",
                    "average faculty performance",
                    "poor involvement in research",
                ]
            )

            w.writerow(
                [
                    exp,
                    designation,
                    salary,
                    publications,
                    book_ch,
                    consultancy,
                    funds,
                    membership,
                    text,
                ]
            )

    print("faculty.csv created.")


# b) Preprocess text (remove punctuation + stopwords)
stop_words = {"and", "the", "in", "on", "is", "a", "an", "of", "for"}


def clean_text(text):
    text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = [w for w in text.split() if w not in stop_words]
    return " ".join(words)


# c) Convert to TF-IDF vectors + Train Naive Bayes
def train_model():
    texts = []
    labels = []

    with open("faculty.csv") as f:
        r = csv.reader(f)
        next(r)
        for row in r:
            cleaned = clean_text(row[-1])
            texts.append(cleaned)

            # Assign class label based on text
            if "excellent" in cleaned or "good" in cleaned:
                labels.append(1)  # positive
            else:
                labels.append(0)  # negative

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    y = labels

    model = MultinomialNB()
    model.fit(X, y)

    print("Model Training Completed.")
    print("Example Prediction:", model.predict(X[:5]))


# -------- MAIN EXECUTION --------
generate_faculty_csv()
train_model()
