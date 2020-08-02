#! python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='tqUqut137XpZTA',
                    client_secret='	xrp_X7Ahz7KDd8i6O7IFmjMYfvg',
                    user_agent='Example App for CPE106L Class',
                    username='Onat_Ignacio',
                    password='asdasdfasdf')

                    subreddit = reddit.subreddit('livestreamfail')
                    top_subreddit = subreddit.top(limit=50)

topics_dict = {"title":[],"score":[],"id":[],"url":[],"comms_num":[],"created":[],"body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created
    topics_dict["body"].append(submission.selftext)

topic_data = pd.DataFrame(topics_dict)

def get_date(created):

_timestamp = topics_data["created"].apply(get_date)
topics_data = topics_data.assign(timestamp=_timestamp)
topics_data.to_csv('LivestreamFail.csv', index=False)