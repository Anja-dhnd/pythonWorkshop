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
headlines = {
    submission.title
    for submission in reddit.subreddit('politics').hot(limit=None)
}

print(len(headlines))

df = pd.DataFrame(headlines)
df.head()
# print(df)


# df.to_csv('headlines.csv', header=False, encoding='utf-8', index=False)


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

# creating new label to simplify values

df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1

df2 = df[['headline', 'label']]

df2.to_csv('reddit_headlines_labels.csv', encoding ='utf-8', index =False)

df.label.value_counts()

df.label.value_counts(normalize=True) * 100

print('Positive headlines:\n')
pprint(list(df[df['label'] == 1].headline)[:5], width=200)

print('\nNegative headlines:\n')
pprint(list(df[df['label'] == -1].headline)[:5], width=200)

# graph 

fig, ax = plt.subplots(figsize=(8,8))
counts = df.label.value_counts(normalize=True) * 100

sns.barplot(x=counts.index, y=counts, ax=ax)

ax.set_xticklabels(['Negative', 'Neutral', 'Positive'])
ax.set_ylabel('Percentage')

plt.show()
