import twarc
import json


def get_twitter_api_credentials():
    with open('../data/twitter_credentials.txt') as json_file:
        data = json.load(json_file)
    consumer_key = data['consumer_key']
    consumer_secret = data['consumer_secret']
    access_token = data['access_token']
    access_token_secret = data['access_token_secret']
    return consumer_key, consumer_secret, access_token, access_token_secret


def get_twarc_object(consumer_key, consumer_secret, access_token, access_token_secret):
    return twarc.Twarc(consumer_key, consumer_secret, access_token, access_token_secret)


def get_tweet_json(file_name, range_start, range_end, output_file_name, twarc_t):
    with open(file_name) as tweet_file:
        tweet_ids = tweet_file.readlines()[range_start: range_end]

    tweets = list(twarc_t.hydrate(tweet_ids))
    with open(output_file_name, 'w') as outfile:
        json.dump(tweets, outfile)


def main():
    consumer_key, consumer_secret, access_token, access_token_secret = get_twitter_api_credentials()
    twarc_t = get_twarc_object(consumer_key, consumer_secret, access_token, access_token_secret)
    input_file_name = "../data/tweet_ids/climate_id.txt.00"
    range_start = 0
    range_end = 15
    output_file_name = "../data/tweets/tweet_" + input_file_name[-2:] + "_" + str(range_start) + "_" + str(
        range_end) + ".txt"
    get_tweet_json(input_file_name, range_start, range_end, output_file_name, twarc_t)


if __name__ == "__main__":
    main()
