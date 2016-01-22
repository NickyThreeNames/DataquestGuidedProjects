import pandas as pd

def load_data():
    a = pd.read_csv('hn_stories.csv')
    a.columns = ['submission_time', 'upvotes', 'url', 'headline']
    return a
