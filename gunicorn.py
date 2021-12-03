wsgi_app = react-auth.wsgi.application

workers=3

bind = 0.0.0.0:8000
reload=True

daemon=True