from turtle import pen
from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.linear_model import LogisticRegression
import numpy as np


HUGGINGFACE_ID = 'sentence-transformers/all-mpnet-base-v2'


class Classifier:
    def __init__(self):
        self.device = torch.device(
            'cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = AutoTokenizer.from_pretrained(HUGGINGFACE_ID)
        self.encoder = AutoModel.from_pretrained(
            HUGGINGFACE_ID).to(self.device)
        self.classifier = None

    def get_embedding(self, text):
        tokens = torch.tensor(self.tokenizer.encode(text)
                              ).unsqueeze(0).to(self.device)
        embeddings = self.encoder(tokens)[0]
        return embeddings[0, 0].cpu().detach().numpy()

    def train(self, dataset):
        train_X = []
        train_y = []

        for text, label in dataset.items():
            embedding = self.get_embedding(text)
            train_X.append(embedding)
            train_y.append(label)

        train_X = np.array(train_X)
        train_y = np.array(train_y)

        self.classifier = LogisticRegression(
            max_iter=2000,
            penalty='l2',
            solver='lbfgs',
            multi_class='multinomial'
        )
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
    pickle.dump(classifier.classifier, open('classifier.pkl', 'wb'))
