from twitter import Twitter
from classifier import Classifier
import pickle
import sys
import numpy as np

if __name__ == '__main__':
    t = Twitter()
    classifier = Classifier()
    classifier.classifier = pickle.load(open('classifier.pkl', 'rb'))

    query = sys.argv[1]
    num_tweets = int(sys.argv[2])
    target_label = int(sys.argv[3])

    already_checked = set()

    profiles = t.profiles_from_search(query, num_tweets)
    for profile in profiles:
        text = str(profile)
        if text not in already_checked:
            logits = classifier.predict(str(profile))
            prediction = np.argmax(logits)

            if prediction == target_label:
                print('https://twitter.com/%s' % profile.username)

            already_checked.add(text)
