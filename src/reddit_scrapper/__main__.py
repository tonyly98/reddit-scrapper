import praw
from models.data_conversion import export_json, export_csv
import argparse
from datetime import datetime, timezone


parser = argparse.ArgumentParser(
    description="Provide databack as json or sql"
)

# Client ID from reddit app
parser.add_argument(
    "-id", "--client_id", metavar="client_id",
    required=True, help= "The client ID of your app"
)

# Client secret from reddit app
parser.add_argument(
    "-secret", "--client_secret", metavar="client_secret",
    required=True, help= "The client ID of your app"
)

# Agent name for reddit 
parser.add_argument(
    "-agent", "--user_agent", metavar="user_agent",
    required=True, help= "The client ID of your app"
)

# Format of exporting
parser.add_argument(
    "-data", "--datatype", metavar="datatype",
    required=False, default="json",help= "Return as CSV or json"
)


args = parser.parse_args()
print(args.datatype)
#    client_id="dX5FicqjbH7MM2nwlHnL3Q",
#    client_secret="lgzyJMsDBpQDsnHeW0Z-FNiEWQA5Cg",
#    user_agent="cute-subreddit-scrapper"
reddit = praw.Reddit(
    client_id=args.client_id,
    client_secret=args.client_secret,
    user_agent=args.user_agent
)

# Setting up for gathering info from post
submission_list = []
for submission in reddit.subreddit("all").top(time_filter="week", limit=10):
    temp_dict = {
        "subreddit": submission.subreddit.display_name,
        "id": submission.id,
        "date": datetime.fromtimestamp(submission.created_utc, timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
        "author": submission.author.name,
        "title": submission.title,
        "score": submission.score,
        "url": submission.url
    }
    submission_list.append(temp_dict)
    
export_json(submission_list)
export_csv(submission_list)
