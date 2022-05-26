from waitress import serve

from django-project.taskmate.taskmate.wsgi import application

if __name__ == '__main__':
    serve(application)
