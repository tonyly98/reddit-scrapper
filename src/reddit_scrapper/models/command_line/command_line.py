import argparse
import praw

def parser():
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
        required=True, help= "The client secret of your app"
    )

    # Agent name for reddit 
    parser.add_argument(
        "-agent", "--user_agent", metavar="user_agent",
        required=True, help= "The client name of your app"
    )

    # Subbreddit to scrape from
    parser.add_argument(
        "-sub", "--subreddit", metavar="subreddit",
        required=False, default="all",help= "Subreddit to scrape from"
    )

    # Sort by order 
    parser.add_argument(
        "-sort", "--sort_by", metavar="sort_by", choices=['hot', 'new', 'top', 'rising', 'controversial'],
        required=False, default="hot",help= "Sort by order of subreddit, default is hot (hot, new, top, rising, controversial)"
    )

    # Time frame (only need for top and controversial sort oders)
    parser.add_argument(
        "-frame", "--time_frame", metavar="time_frame",
        required=False, default="month", choices=["all", "day", "hour", "month", "week", "year"],
        help= 'Time frame, only need for top and controversial sort oders, default is month ("all", "day", "hour", "month", "week", or "year")'
    )

    # Number of post
    parser.add_argument(
        "-limit", "--limit", metavar="limit", type=int,
        required=False, default=100,help= "The number of posts returns, the default is 100, anything over 100 could be unstable"
    )

    # Format of exporting
    parser.add_argument(
        "-data", "--datatype", metavar="datatype",
        required=False, default="json",help= "Return as CSV or json"
    )
    
    return parser.parse_args()

def subreddits_parser(args: argparse.Namespace, reddit: praw.reddit.Reddit):
    if args.sort_by == "hot":
        return reddit.subreddit(args.subreddit).hot(limit=args.limit)
    elif args.sort_by == "new":
        return reddit.subreddit(args.subreddit).new(limit=args.limit)
    elif args.sort_by == "rising":
        return reddit.subreddit(args.subreddit).new(limit=args.limit)
    elif args.sort_by == "top":
        return reddit.subreddit(args.subreddit).top(time_filter=args.time_frame,limit=args.limit)
    else:
        return reddit.subreddit(args.subreddit).controversial(time_filter=args.time_frame,limit=args.limit)