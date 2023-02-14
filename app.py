from flask import Flask, render_template
from cluster_links import *

app = Flask(__name__)

links = [
        'https://www.gorillatoursafrica.com/things-to-do-in-kigali/',
        'https://www.thetravelersbuddy.com/2022/08/30/best-things-rwanda/',
        'https://www.silverbackgorillatours.com/rwanda/tourist-attractions-in-kigali',
        'https://news.google.com/',
        'https://edition.cnn.com/',
        'https://www.nbcnews.com/',
        'https://www.bbc.com/news',
        'https://www.foxnews.com/',
        'https://www.silverbackgorillatours.com/rwanda/tourist-attractions-in-kigali',
        'https://news.google.com/',
        'https://edition.cnn.com/',
        'https://www.nbcnews.com/',
    ]

@app.route("/")
def show_clusters():
    # Cluster the articles into groups based on their content
    cluster_labels = cluster_news_articles(links)

    # Organize the articles by cluster
    clusters = {}
    for i, link in enumerate(links):
        label = cluster_labels[i]
        if label not in clusters:
            clusters[label] = []
        clusters[label].append((i + 1, link))

    # Render the results template, passing in the clusters
    return render_template("results.html", clusters=clusters)

if __name__ == "__main__":
    app.run()
