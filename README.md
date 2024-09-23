# Welcome to reddit-scrapper!
reddit-scrapper is a command line script that allows you to scrape posts and export the data as JSON or CSV.
## Installation
Download the latest release and install the latest verison of PRAW via pip.

```sh
pip install praw
```

Setup a [reddit app](https://www.reddit.com/prefs/apps) and input mandatory app keys:
```sh
py reddit_scrapper.zip -id "app-id" -secret "app-secret" -agent "app-name"
```
The full list of possible arguments can be found in [data_conversion.py](https://github.com/tonyly98/reddit-scrapper/blob/main/src/reddit_scrapper/models/data_conversion/data_conversion.py)
