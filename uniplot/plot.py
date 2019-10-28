import matplotlib
import matplotlib.pyplot as plt
matplotlib.axes.Axes.pie


def plot_bar_show(d):
    """Returns a bar chart of given values"""
    r = range(0, len(d))
    ## Prepare a figure
    plt.figure()

    ## Add bars, one at each x position, with the values of d
    plt.bar(r, d.values())
    ## Add labels to the x-axis, with the keys of d
    plt.xticks(r, d.keys())
    ##Squash everything up so there is no white space
    plt.tight_layout()
    ## Show the graph
    plt.show()

def plot_pie_show(d):
    """Returns a pie chart of given values"""
    r = range(0, len(d))
    labels = plt.xticks(r, d.keys())
    sizes = plt.pie(r, d.values())

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=0, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()




