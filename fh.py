from flask import Flask, request, render_template
from utils import parse, plot_sbg_results
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data_url = request.form['csvurl']
    sbg_results = parse(data_url)
    script, div = plot_sbg_results(sbg_results)
    return render_template('results.html', results=sbg_results, plot_script=script, plot_area=div)


if __name__ == '__main__':
    app.run()
