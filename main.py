from crawler import Crawler
from classifier import Classifier
import pickle
import sys

if __name__ == '__main__':
    classifier = pickle.load(open('classifier.pkl', 'rb'))

    query = sys.argv[1]
    num_tweets = int(sys.argv[2])
    target_label = int(sys.argv[3])
    min_prob = float(sys.argv[4])

    crawler = Crawler(classifier, target_label, min_prob, query, num_tweets)

    while crawler.step():
        # continue crawling
        pass
