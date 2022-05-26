from waitress import serve

from taskmate.wsgi import application

if __name__ == '__main__':
    serve(application)
