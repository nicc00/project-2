import pandas as pd
import matplotlib.pyplot as plt


def avgWordPlot(input_file):
    """
    Return a plot comparing average words per comment.

    Args:
        input_file: name of input file
    """
    plot_test = pd.read_csv(input_file)
    subs = plot_test['Subreddit'].values.tolist()
    top = plot_test['"Top" Average Words'].values.tolist()
    hot = plot_test['"Hot" Average Words'].values.tolist()
    plt.style.use('ggplot')
    plt.bar(subs, top, align='edge', width=-.4, label='Top')
    plt.bar(subs, hot, align='edge', width=.4, label='Hot')
    plt.xlabel('Subreddit')
    plt.ylabel('Average words per comment')
    plt.title('Average words per comment, 150 posts')
    plt.legend(loc='upper left')
    plt.show


def correctnessPlot(input_file):
    """
    Return a plot comparing spelling correctness.

    Args:
        input_file: name of input file
    """
    plot_test = pd.read_csv(input_file)
    subs = plot_test['Subreddit'].values.tolist()
    top = plot_test['"Top" % of correct words'].values.tolist()
    hot = plot_test['"Hot" % of correct words'].values.tolist()
    plt.style.use('ggplot')
    plt.bar(subs, top, align='edge', width=-.4, label='Top')
    plt.bar(subs, hot, align='edge', width=.4, label='Hot')
    plt.ylim(0, 1)
    plt.xlabel('Subreddit')
    plt.ylabel('Percent of correct words per comment')
    plt.title('Percent of correct words per comment, 50 posts')
    plt.legend(loc='upper left')
    plt.show
