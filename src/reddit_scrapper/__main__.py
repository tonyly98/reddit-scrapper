import praw
import json

reddit = praw.Reddit(
    client_id="your id heree",
    client_secret="your secret key here",
    user_agent="cute-subreddit-scrapper",
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
    
# serializing info    
jsonInfo = json.dumps(submission_list, indent=4)

# writing to file
with open("test.json", "w") as json_file:
    json_file.write(jsonInfo)
    print("Saved!")
    
