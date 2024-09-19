import praw
import json
import csv
from models.data_conversion import export_json, export_csv

reddit = praw.Reddit(
    client_id="your id heree",
    client_secret="your secret key here",
    user_agent="cute-subreddit-scrapper"
)

# Setting up for gathering info from post
submission_list = []
for submission in reddit.subreddit("aww").top(time_filter="week", limit=10):
    temp_dict = {
        "id": submission.id,
        "subreddit": submission.subreddit.display_name,
        "title": submission.title,
        "author": submission.author.name,
        "score": submission.score,
        "date": submission.created_utc,
        "url": submission.url
    }
    submission_list.append(temp_dict)
    
export_json(submission_list)
export_csv(submission_list)