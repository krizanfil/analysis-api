from flask import Flask, request
from helpers.data_processing import process_ticker, analyses_result

app = Flask(__name__)


@app.route('/api/analyze/<string:ticker>', methods=['GET'])
def get(ticker: str) -> analyses_result:
    return process_ticker(ticker)


@app.route('/api/analyze_list', methods=['POST'])
def post():
    tickers = request.json['tickers']
    return {"results": [process_ticker(ticker) for ticker in tickers]}


if __name__ == "__main__":
    app.run(debug=True)
