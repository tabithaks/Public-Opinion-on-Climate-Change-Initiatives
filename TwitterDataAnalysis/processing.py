import pandas as pd
import numpy as np
import re
import string

def get_entities(twitter_data, column = "hashtags"):
    twitter_data = twitter_data.copy()
    #twitter_data[column] = twitter_data[column].apply(eval)
    return [hashtag for hashtags in list(twitter_data[column]) for hashtag in hashtags]

def get_cols(twitter_data, column = "full_text"):
    twitter_data['hashtags'] = twitter_data['full_text'].apply(lambda x: re.findall(r"#(\w+)", x))
    twitter_data['mentions'] = twitter_data['full_text'].apply(lambda x: re.findall(r"@(\w+)", x))
    twitter_data['full_text'] = twitter_data['full_text'].str.replace(r'http\S+', '', regex=True)
    twitter_data["created_at"] = pd.to_datetime(twitter_data["created_at"])

#combines clean_text_round1 and clean_text_round2 from Starter Exploratory Analysis Notebook
def clean_text_lda(text):
    '''Make text lowercase, remove text in square brackets, remove punctuation and remove words containing numbers.'''
    text = text.lower()
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text) #get rid of all punctuation
    text = re.sub('\w*\d\w*', '', text) #\d is all digits, w is alphanumeric characters * is 0 or more times
    text = re.sub('[‘’“”…]', '', text)  # get rid of all the quotes
    text = re.sub('\n', '', text)  # get rid of line breaks \n
    return text

#from https://scikit-learn.org/stable/auto_examples/applications/plot_topics_extraction_with_nmf_lda.html
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
