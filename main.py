from crawler import Crawler
import pickle
import sys

if __name__ == '__main__':
    classifier = pickle.load(open('classifier.pkl', 'rb'))

    query = sys.argv[1]
    num_tweets = int(sys.argv[2])
    target_label = int(sys.argv[3])

    crawler = Crawler(classifier, target_label, query, num_tweets)

    while crawler.step():
        # continue crawling
        pass
