from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import nltk
from pprint import pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import praw

user_agent = "Scraper 1.0"
reddit = praw.Reddit(
    client_id="9alNpa66PPgwK9WRepyZxA",
    client_secret="DgfKOtW36RX6kDEvGyXx6wxCCZW7sA",
    user_agent=user_agent
)
# scrapping data
headlines = set()
for submission in reddit.subreddit('politics').hot(limit=None):
    headlines.add(submission.title)
    # print(submission.title)
    # print(submission.id)
    # print(submission.author)
    # print(submission.created_utc)
    # print(submission.score)
    # print(submission.upvote_ratio)
    # print(submission.url)
    # break
print(len(headlines))


df = pd.DataFrame(headlines)
df.head()
# print(df)

df.to_csv('headlines.csv', header=False, encoding='utf-8', index=False)


nltk.download('vader_lexicon')


sia = SIA()
results = []

for line in headlines:
    pol_score = sia.polarity_scores(line) # return a dico
    pol_score['headline'] = line
    results.append(pol_score)
    
pprint(results[:5], width=100)

# putting results in a frame

df = pd.DataFrame.from_records(results)
df.head()