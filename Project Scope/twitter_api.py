import tweepy


class TwitterAPI:
    def __init__(self, api_key, api_secret_key, access_token,
                 access_token_secret):
        # Replace with your Twitter API credentials
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret_key,
                                             access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def get_user_data(self, username):
        try:
            user = self.api.get_user(screen_name=username)
            return {
                "followers_count": user.followers_count,
                "tweets_count": user.statuses_count,
                "bio": user.description,
                "username": user.screen_name,
            }
        except Exception as e:
            print(f"Error fetching Twitter data: {e}")
            return None
