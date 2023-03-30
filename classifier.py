from sklearn.linear_model import LogisticRegression
import numpy as np
import openai
from caching import Cache
import dotenv
import os

dotenv.load_dotenv()

MODEL_ID = "text-embedding-ada-002"
cache = Cache('embeddings.pkl')

openai.api_key = os.getenv('OPENAI_API_KEY')


class Classifier:
    def __init__(self):
        self.classifier = None

    def get_embedding(self, text):
        if hash(text) in cache.data:
            return cache.data[hash(text)]
        
        text = text.replace("\n", " ").replace("\r", " ")
        embedding = openai.Embedding.create(input=[text], model=MODEL_ID)['data'][0]['embedding']
        cache.data[hash(text)] = embedding

        return embedding

    def train(self, dataset):
        train_X = []
        train_y = []

        for text, label in dataset.items():
            embedding = self.get_embedding(text)
            train_X.append(embedding)
            train_y.append(label)

        train_X = np.array(train_X)
        train_y = np.array(train_y)

        self.classifier = LogisticRegression()
        self.classifier.fit(train_X, train_y)

    def predict(self, text):
        embedding = self.get_embedding(text)
        return self.classifier.predict_proba([embedding])[0]


if __name__ == '__main__':
    import json

    classifier = Classifier()
    with open('dataset.json', 'r') as f:
        dataset = json.load(f)

    import pickle
    classifier.train(dataset)
    pickle.dump(classifier, open('classifier.pkl', 'wb'))

    cache.save()
