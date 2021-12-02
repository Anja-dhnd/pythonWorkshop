import pandas as pd
import numpy as np
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import seaborn as sn
from IPython import display
from pprint import pprint
import praw

nltk.download('vader_lexicon')
nltk.download('stopwords')

sn.set(style='darkgrid', context='talk', palette='Dark2')

