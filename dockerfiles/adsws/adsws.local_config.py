import os

# Automatically generated by: python manage.py create_local_config

SOLR_SEARCH_HANDLER = 'http://adswhy:9000/solr/select'
SOLR_QTREE_HANDLER = 'http://adswhy:9000/solr/qtree'
SOLR_UPDATE_HANDLER = 'http://adswhy:9000/solr/update'


CORS_DOMAINS = {
                'http://adslabs.org': 1,
		'http://localhost:8000': 1,
		'http://localhost:5000': 1
                }

SECRET_KEY = 'fake'
ACCOUNT_VERIFICATION_SECRET = 'fake'

DEBUG = False
TESTING = False

# Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
SQLALCHEMY_ECHO = False

CLASSIC_LOGIN_URL = 'http://adsabs.harvard.edu/cgi-bin/maint/manage_account/credentials'

SITE_SECURE_URL = 'http://0.0.0.0:5000'



SQLALCHEMY_DATABASE_URI = 'sqlite:////adsws/adsws.sqlite'
print os.environ
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://adsws:adsws@'+os.environ.get('POSTGRESQL_PORT_5432_TCP_ADDR', 'localhost') + ':' + os.environ.get('POSTGRESQL_PORT_5432_TCP_PORT', '5432') + '/adsws'


OAUTH2_CACHE_TYPE='simple'


import logging
logging.basicConfig(level=logging.DEBUG)

# Stuff that should be added for every application
CORE_PACKAGES = []

FALL_BACK_ADS_CLASSIC_LOGIN = True
