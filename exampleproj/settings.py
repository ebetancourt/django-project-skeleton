import sys

try:
    from settings_local import *
except ImportError:
    if 'runserver' in sys.argv or 'runserver_plus' or 'syncdb' in sys.argv:
        from conf.development import *
    else:
        from conf.staging import *