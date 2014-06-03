from __future__ import unicode_literals

import os

#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()


import sys
 
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'kidsupper2.settings'
 
virtenv = os.environ['OPENSHIFT_HOMEDIR'] + 'python-2.6/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
 
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except IOError:
    pass
#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()