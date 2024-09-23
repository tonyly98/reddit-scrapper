import praw
from models.data_conversion import export_json, export_csv
from models.command_line import parser, subreddits_parser
from datetime import datetime, timezone

args = parser()
print(type(args.limit))
print(args.limit)

reddit = praw.Reddit(
    client_id=args.client_id,
    client_secret=args.client_secret,
    user_agent=args.user_agent
)
print(type(reddit))

# Setting up for gathering info from post
submission_list = []
subreddits = subreddits_parser(args, reddit)

for submission in subreddits:
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

if args.datatype == "json":    
    export_json(submission_list)
else:
    export_csv(submission_list)
