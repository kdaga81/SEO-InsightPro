from flask import Flask
import findWordCount
import DataScraper
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# yet to complete dont run this
url = input("Enter the URL you want to scrape: ")
scrapped_data = DataScraper.getWepageData(url)
algorithmselected = input("NaiveStringMatching  KMPAlgorithm  RabinKarbAlgorithm")


@app.route("/")
def sendProcessTimeAndWordCountand():
    wordCount, process_time = findWordCount.getProcessTimeAndWordCount(
        scrapped_data, algorithmselected
    )
    return [wordCount, process_time]


if __name__ == "__main__":
    app.run()
