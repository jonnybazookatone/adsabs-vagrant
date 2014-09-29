
# Automatically generated by: python manage.py create_local_config

SOLR_SEARCH_HANDLER = 'http://localhost:9000/solr/select'
SOLR_QTREE_HANDLER = 'http://localhost:9000/solr/qtree'
SOLR_UPDATE_HANDLER = 'http://localhost:9000/solr/update'

ANONYMOUS_USER = 'anonymous@adslabs.org'

EXTENSIONS = ['adsws.ext.menu',
              'adsws.ext.sqlalchemy',
              'adsws.ext.security',]

PACKAGES = ['adsws.modules.oauth2server',
            'adsws.api.solr',
            'adsws.api.bumblebee']

CORS_DOMAINS = {
                'http://adslabs.org': 1
                }

SECRET_KEY = ''
ACCOUNT_VERIFICATION_SECRET = ''

DEBUG = False
TESTING = False

# Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
SQLALCHEMY_ECHO = False

CLASSIC_LOGIN_URL = 'http://adsabs.harvard.edu/cgi-bin/maint/manage_account/credentials'

SITE_SECURE_URL = 'http://0.0.0.0:5000'



SQLALCHEMY_DATABASE_URI = 'sqlite:////adsws/adsws.sqlite'

OAUTH2_CACHE_TYPE='simple'


import logging
logging.basicConfig(level=logging.DEBUG)

# Stuff that should be added for every application
CORE_PACKAGES = []
