from twitter import Twitter
import numpy as np


class Crawler:
    def __init__(self, classifier, target_label, query, num_tweets, max_queue_size=1000):
        self.twitter = Twitter()
        self.queue = self.twitter.profiles_from_search(query, num_tweets)
        self.max_queue_size = max_queue_size
        self.already_checked = set()
        self.classifier = classifier
        self.target_label = target_label

    # returns True if it should continue crawling
    def step(self):
        # make sure the queue is not empty
        if len(self.queue) != 0:
            current = self.queue[0]
            self.queue = self.queue[1:]
            if current.username not in self.already_checked:
                self.already_checked.add(current.username)

                # check if the profile is of the target label
                logits = self.classifier.predict(str(current))
                prediction = np.argmax(logits)

                if prediction == self.target_label:
                    # if it is, print the profile
                    print('https://twitter.com/%s' % current.username)

                    if len(self.queue) < self.max_queue_size:
                        # add mentioned profiles to the queue
                        profiles = self.twitter.profiles_from_profile(current)
                        for profile in profiles:
                            if profile.username not in self.already_checked:
                                self.queue.append(profile)
            return True
        
        return False
