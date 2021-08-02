from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@app.route('/04_contact')
def contact():
    return flask.render_template('04_contact.html')

@app.route('/03_about')
def about():
    return flask.render_template('03_about.html')

@app.route('/02_product')
def product():
    return flask.render_template('02_product.html')

@app.route('/01_project')
def project():
    return flask.render_template('01_project.html')



@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
