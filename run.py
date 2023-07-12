import os
from os.path import join, dirname

from dotenv import load_dotenv
from werkzeug.serving import run_simple
from werkzeug.routing import Map, Rule, Submount
from werkzeug.wrappers import Request, Response
from werkzeug.exceptions import HTTPException

from property import get_properties

dotenv_path = join(dirname(__file__), '.env.local')
load_dotenv(dotenv_path)

# CONSTANTS
DEBUG = os.getenv('DEBUG')

# HOME
def home(request: Request):
    return Response('Hello, World')

class PropertyApp(object):
    def __init__(self):
        self.url_map = Map([
            Rule('/', endpoint=home),
            Submount('/properties', [
                Rule('/', methods=['GET'], endpoint=get_properties),
    ])
])

    def dispatch_request(self, request):
        map_adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = map_adapter.match()
            return endpoint(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

def create_app():
    return PropertyApp()


if __name__ == '__main__':
    application = create_app()
    run_simple('127.0.0.1', 5000, application, use_debugger=DEBUG, use_reloader=True)