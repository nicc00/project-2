import praw
import pandas as pd


def submissionAverageCalculator(submission):
    """
    Return the average comment length of a submission.

    Args:
        submission: A reddit post.
    """
    total_comment_length = 0
    comment_count = 0
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        split_comment = comment.body.split()
        comment_length = len(split_comment)
        total_comment_length += comment_length
        comment_count += 1
    if comment_count == 0:
        return 0
    else:
        avg_comment_length = total_comment_length / comment_count
    return avg_comment_length


def subredditTopAverages(subreddit, limit):
    """
    Return the average comment length of a subreddit's top posts.

    Args:
        subreddit: A subreddit.
        limit: How many posts to include.
    """
    sub_avg_tot = 0
    for submission in subreddit.top(limit=limit):
        sub_avg_tot += submissionAverageCalculator(submission)
    sub_avg = sub_avg_tot / limit
    return sub_avg


def subredditHotAverages(subreddit, limit):
    """
    Return the average comment length of a subreddit's hot posts.

    Args:
        subreddit: A subreddit.
        limit: How many posts to include.
    """
    sub_avg_tot = 0
    for submission in subreddit.hot(limit=limit):
        submissionAverageCalculator(submission)
        sub_avg_tot += submissionAverageCalculator(submission)
    sub_avg = sub_avg_tot / limit
    return sub_avg


def getAverages(subreddits, limit, output_file):
    """
    Return the average comment lengths of certain subreddits.

    Args:
        subreddits: A list of subreddits.
        limit: How many posts to include.
        output_file: Name of file to save data to.

    Returns a csv file of the "top" and "hot" averages of a list of subreddits
    in the form of a dataframe.
    """
    avg_dict = {}
    top_avgs = []
    hot_avgs = []
    for i in range(len(subreddits)):
        current_sub = reddit.subreddit(subreddits[i])
        top_avgs.append(subredditTopAverages(current_sub, limit))
        hot_avgs.append(subredditHotAverages(current_sub, limit))
    avg_dict['Subreddit'] = subreddits
    avg_dict['"Top" Average Words'] = top_avgs
    avg_dict['"Hot" Average Words'] = hot_avgs
    word_scores = pd.DataFrame(avg_dict)
    word_scores.to_csv(output_file)
    return word_scores
