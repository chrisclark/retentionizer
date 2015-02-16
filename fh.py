from flask import Flask, request, render_template, url_for
from utils import parse, plot_sbg_results, plot_sbg_retention_distribution
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data_url = request.form.get('csvurl') or request.form.get('samples')
    periods = request.form.get('periods') or 4
    sbg_results = parse(data_url, periods)
    script, div = plot_sbg_results(sbg_results)
    distribution_script, distribution_div = plot_sbg_retention_distribution(sbg_results)
    return render_template('results.html', results=sbg_results,
                           plot_script=script, plot_area=div,
                           plot_distribution_script=distribution_script, plot_distribution_area=distribution_div)


if __name__ == '__main__':
    app.debug = True
    app.run()
