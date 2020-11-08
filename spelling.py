import praw
import pandas as pd
from spellchecker import SpellChecker


def getTopComments(subreddit, limit):
    """
    Return a list of every word in every comment in top submissions.

    Args:
        subreddit: The name of the subreddit.
        limit: How many posts to include.
    """
    current_sub = reddit.subreddit(subreddit)
    comment_list = []
    for submission in current_sub.top(limit=limit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            split_comment = comment.body.split()
            comment_list.append(split_comment)
    return comment_list


def getHotComments(subreddit, limit):
    """
    Return a list of every word in every comment in hot submissions.

    Args:
        subreddit: The name of the subreddit.
        limit: How many posts to include.
    """
    current_sub = reddit.subreddit(subreddit)
    comment_list = []
    for submission in current_sub.hot(limit=limit):
        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():
            split_comment = comment.body.split()
            comment_list.append(split_comment)
    return comment_list


def spellChecker(comment_list):
    """
    Return the percent of words in a list that are spelled correctly.

    Args:
        comment_list: A list of words.
    """
    correct_words = 0
    total_words = 0
    spell = SpellChecker()
    for i in range(len(comment_list)):
        for x in range(len(comment_list[i])):
            if isinstance(comment_list[i][x], str):
                if comment_list[i][x] in spell:
                    correct_words += 1
                total_words += 1
    if total_words == 0:
        return 0
    else:
        percent_correct = correct_words / total_words
    return percent_correct


def spellingComparer(subreddits, limit, output_file):
    """
    Return the spelling correctness of subreddits.

    Args:
        subreddits: List of subreddits to spell check.
        limit: How many posts to include.
        output_file: Name of output file.

    Returns a csv file of the percent of correct words in each subreddit's hot
    and top categories.
    """
    correctness_dict = {}
    top_correctness = []
    hot_correctness = []
    for i in range(len(subreddits)):
        top_comments = getTopComments(subreddits[i], limit)
        hot_comments = getHotComments(subreddits[i], limit)
        top_correctness.append(spellChecker(top_comments))
        hot_correctness.append(spellChecker(hot_comments))
    correctness_dict['Subreddit'] = subreddits
    correctness_dict['"Top" % of correct words'] = top_correctness
    correctness_dict['"Hot" % of correct words'] = hot_correctness
    spelling_scores = pd.DataFrame(correctness_dict)
    spelling_scores.to_csv(output_file)
    return spelling_scores
