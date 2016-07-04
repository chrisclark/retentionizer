from flask import Flask, request, render_template
from utils import parse, plot_sbg_results, plot_sbg_retention_distribution
from hashlib import sha1
import time, os, json, base64, hmac, urllib

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.form.get('uploaded_csv_url'):
        data_url = request.form.get('uploaded_csv_url')
    else:
        data_url = request.form.get('csvurl') or request.form.get('samples')
    periods = request.form.get('periods') or 4
    periods = int(periods)
    discount = request.form.get('discount') or 10
    discount = float(discount) / 100.0
    value = request.form.get('value') or 10
    value = float(value)

    sbg_results = parse(data_url, periods, discount, value)
    script, div = plot_sbg_results(sbg_results)
    distribution_script, distribution_div = plot_sbg_retention_distribution(sbg_results)

    return render_template('results.html', results=sbg_results,
                           plot_script=script, plot_area=div,
                           plot_distribution_script=distribution_script, plot_distribution_area=distribution_div)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/sign_s3/')
def sign_s3():
    AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
    S3_BUCKET = os.environ.get('S3_BUCKET')

    object_name = request.args.get('s3_object_name')
    mime_type = request.args.get('s3_object_type')

    expires = long(time.time()+1000)
    amz_headers = "x-amz-acl:public-read"

    put_request = "PUT\n\n%s\n%d\n%s\n/%s/%s" % (mime_type, expires, amz_headers, S3_BUCKET, object_name)

    signature = base64.encodestring(hmac.new(AWS_SECRET_KEY, put_request, sha1).digest())
    signature = urllib.quote_plus(signature.strip())

    url = 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, object_name)

    return json.dumps({
        'signed_request': '%s?AWSAccessKeyId=%s&Expires=%d&Signature=%s' % (url, AWS_ACCESS_KEY, expires, signature),
         'url': url
      })


if __name__ == '__main__':
    app.debug = True
    app.run()
