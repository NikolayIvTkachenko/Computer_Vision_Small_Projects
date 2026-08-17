# pip install sklearn
# https://archive.ics.uci.edu/ml/index.php
# Machine Lerning Repository UC Irvine ==> Sentiment Labelled Sentences
# sentiment labelled sentences.zip

# https://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences

# import kagglehub

# Download latest version
# path = kagglehub.dataset_download("marklvl/sentiment-labelled-sentences-data-set")

# print("Path to dataset files:", path)

# Path to dataset files: C:\Users\RobotComp.ru\.cache\kagglehub\datasets\marklvl\sentiment-labelled-sentences-data-set\versions\2

print("=========================================================================================================================")

import pandas as pd
df = pd.read_csv('data_files/sentiment labelled sentences/amazon_cells_labelled.txt', sep='\t', header=None, names=['review', 'sentiment'] )

print(df.head())

from sklearn.model_selection import train_test_split
reviews = df['review'].values
sentiments = df['sentiment'].values
reviews_train, reviews_test, sentiment_train, sentiment_test = train_test_split(reviews, sentiments, test_size=0.2, random_state=500)

print("1 => -------------------------------")
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
vectorizer.fit(reviews)
X_train = vectorizer.transform(reviews_train)
X_test = vectorizer.transform(reviews_test)

# print(X_train)

print("2 => -------------------------------")

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, sentiment_train)

accuracy = classifier.score(X_test, sentiment_test)
print("Accuracy:", accuracy)

print("3 => -------------------------------")
new_reviews = ['Old version of python useless', 'Very good effort, but not five stars', 'Clear and concise']

X_new = vectorizer.transform(new_reviews)
print(classifier.predict(X_new))



