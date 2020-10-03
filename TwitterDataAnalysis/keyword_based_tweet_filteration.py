import json


def filter_tweets(input_file_name, output_file_dir):
    with open(input_file_name) as tweet_file:
        tweets = json.load(tweet_file)

    tweet_labels = ['paris_agreement', 'green_new_deal', 'climate_change']
    labeled_tweets = {label: [] for label in tweet_labels}
    for tweet in tweets:
        tweet_text = tweet['full_text']
        if "paris" in tweet_text and ("agreement" in tweet_text or "accord" in tweet_text):
            labeled_tweets['paris_agreement'].append(tweet)
        if "green" in tweet_text and "new" in tweet_text and "deal" in tweet_text:
            labeled_tweets['green_new_deal'].append(tweet)
        if "climate" in tweet_text and "change" in tweet_text:
            labeled_tweets['climate_change'].append(tweet)

    for tweet_label in tweet_labels:
        with open(output_file_dir + tweet_label + '.txt', 'a') as outfile:
            json.dump(labeled_tweets.get(tweet_label), outfile)


def main():
    input_file_name = "../data/tweets/tweet_00_0_15.txt"
    output_file_dir = "../data/filtered_tweets/"
    filter_tweets(input_file_name, output_file_dir)


if __name__ == "__main__":
    main()
