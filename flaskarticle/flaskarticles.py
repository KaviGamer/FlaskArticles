from flask import Flask, jsonify, request
import csv

all_articles = []

with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

liked_movies = []
not_liked_movies = []
did_not_watch = []

app = Flask(__name__)

@app.route("/get-movie")
def get_movies():
    return jsonify({
        "data":allmovies[0],
        "status":"success",
    }),200

if __name__ == "__main__": 
    app.run()