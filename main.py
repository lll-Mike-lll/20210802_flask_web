import flask


# Create the application.
APP = flask.Flask(__name__)


@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@APP.route('/04_contact')
def contact():
    return flask.render_template('04_contact.html')

@APP.route('/03_about')
def about():
    return flask.render_template('03_about.html')

@APP.route('/02_product')
def product():
    return flask.render_template('02_product.html')

@APP.route('/01_project')
def project():
    return flask.render_template('01_project.html')


if __name__ == '__main__':
    APP.debug = True
    APP.run(host='127.0.0.1', port=8080, debug=True)
