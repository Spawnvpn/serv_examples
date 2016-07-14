from werkzeug.routing import Rule, Map
from werkzeug.wrappers import Response, Request
from wsgiref.simple_server import make_server


def form(env, **kwargs):
    return Response("String")

urlmap = Map([
    Rule("/", endpoint="index"),
    Rule("/form/<id>", endpoint="form")
])

route = {"form": form}


@Request.application
def app(req):
    urls = urlmap.bind_to_environ(req.environ)
    disp = urls.dispatch(lambda e, v: route[e](req, **v))
    return disp

serv = make_server("", 8080, app)
serv.serve_forever()