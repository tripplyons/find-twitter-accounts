from snscrape.modules.twitter import TwitterHashtagScraper
from classifier import Classifier


class Profile:
    def __init__(self, username, display_name, description):
        self.username = username
        self.display_name = display_name
        self.description = description

    def __str__(self):
        return '%s (@%s):\n%s' % (self.display_name, self.username, self.description)


class Twitter:
    def __init__(self):
        pass

    def profiles_from_tweets(self, tweets):
        profiles = []

        for tweet in tweets:
            user = tweet.user
            profile = Profile(user.username, user.displayname,
                              user.rawDescription)
            profiles.append(profile)

        return profiles

    def profiles_from_hashtag(self, hashtag, num_tweets):
        hashtag_scraper = TwitterHashtagScraper(hashtag)

        generator = hashtag_scraper.get_items()
        tweets = [next(generator) for _ in range(num_tweets)]

        return self.profiles_from_tweets(tweets)


if __name__ == '__main__':
    t = Twitter()
    print(t.profiles_from_hashtag('twitter', 5))
