'''
Author: Joel Rubio
Date: 22-06-2022
'''

from flask import Flask, render_template, jsonify
from articles import ArticleRepository
from logs import Log


app = Flask(__name__)


article_repository = ArticleRepository()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/articles/clothes/details")
def clothes_details():
    response = []
    try:
        response = [article.serialize() for article in article_repository.find_articles_by_clothes_category()]
    except Exception as error:
        Log.print(error)

    return jsonify(response)

@app.route("/articles/accessories/details")
def accessories_details():
    response = []
    try:
        response = [article.serialize() for article in article_repository.find_articles_by_accessories_category()]
    except Exception as error:
        Log.print(error)

    return jsonify(response)

@app.route("/articles/shoes/details")
def shoes_details():
    response = []
    try:
        response = [article.serialize() for article in article_repository.find_articles_by_shoes_category()]
    except Exception as error:
        Log.print(error)

    return jsonify(response)



if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(debug=True)