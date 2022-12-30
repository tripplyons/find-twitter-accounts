from snscrape.modules.twitter import TwitterHashtagScraper, TwitterSearchScraper, TwitterUserScraper


class Profile:
    def __init__(self, username, display_name, description):
        self.username = username
        self.display_name = display_name
        self.description = description

    def __str__(self):
        return '%s, %s, %s' % (self.display_name, self.username, self.description)


class Twitter:
    def __init__(self):
        pass

    def profile_from_user(self, user):
        return Profile(user.username, user.displayname, user.rawDescription)

    def profiles_from_tweets(self, tweets):
        profiles = []

        for tweet in tweets:
            user = tweet.user
            profile = self.profile_from_user(user)
            profiles.append(profile)

        return profiles

    def profiles_from_profile(self, profile, num_tweets=100):
        profile_scraper = TwitterUserScraper(profile.username)

        generator = profile_scraper.get_items()

        tweet_count = 0

        profiles = []
        for tweet in generator:
            if tweet.mentionedUsers is not None:
                for user in tweet.mentionedUsers:
                    new_profile = self.profile_from_user(user)
                    profiles.append(new_profile)

            tweet_count += 1
            if tweet_count >= num_tweets:
                break

        return profiles

    def profiles_from_hashtag(self, hashtag, num_tweets):
        hashtag_scraper = TwitterHashtagScraper(hashtag)

        generator = hashtag_scraper.get_items()
        tweets = [next(generator) for _ in range(num_tweets)]

        return self.profiles_from_tweets(tweets)

    def profiles_from_search(self, search, num_tweets):
        search_scraper = TwitterSearchScraper(search)

        generator = search_scraper.get_items()
        tweets = [next(generator) for _ in range(num_tweets)]

        return self.profiles_from_tweets(tweets)
