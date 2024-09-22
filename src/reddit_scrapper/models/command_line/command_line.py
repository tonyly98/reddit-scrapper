import argparse

class CommandLine():
    
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

# Subbreddit to scrape from
parser.add_argument(
    "-sub", "--subreddit", metavar="subreddit",
    required=False, default="all",help= "Subreddit to scrape from"
)

# Sort by order 
parser.add_argument(
    "-sort", "--sort_by", metavar="sort_by",
    required=False, default="hot",help= "Sort by order of subreddit (hot, new, top, rising, controversial)"
)

# Time frame (only need for top and controversial sort oders)
parser.add_argument(
    "-frame", "--time_frame", metavar="time_frame",
    required=False, default="month",
    help= 'Time frame, only need for top and controversial sort oders ("all", "day", "hour", "month", "week", or "year")'
)

# Number of post
parser.add_argument(
    "-limit", "--limit", metavar="limit",
    required=False, default=100,help= "The number of posts returns, the default is 100, anything over 100 could be unstable"
)

# Format of exporting
parser.add_argument(
    "-data", "--datatype", metavar="datatype",
    required=False, default="json",help= "Return as CSV or json"
)

args = parser.parse_args()
s = "Hello {args.datatype}"
print(s)