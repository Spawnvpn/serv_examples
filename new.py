from wsgiref.simple_server import make_server
from urllib.parse import parse_qs


def form(env):
    cl = int(env.get("CONTENT_LENGTH", "0"))
    d = env['wsgi.input'].read(cl)
    d = parse_qs(d)
    return [d.get('a', '1').encode("UTF-8")]

route = {"form": form}


def app(env, resp_start):
    resp_start("200 OK", [("Content-Type", "text/html")])
    buf = [("%s: %s <br>" % (k, v)).encode('UTF-8') for k, v in env.items()]
    with open("index.html", "r") as f:
        qs = env.get("QUERY_STRING", '')
        qs_d = parse_qs(qs)
        html = (f.read() % (qs_d.get('a'),)).encode("UTF-8")
        result = None
        path = env.get("PATH_INFO", '')[1:]
        parts = path.split("/")
        print(parts[0])
        if len(parts) > 0 and parts[0]:
            fn = route.get(parts[0])
            if fn is not None:
                result = fn(env)
                # with open("index.html", "r") as f:
                #     result = (f.read() % (result,)).encode("UTF-8")
        else:
            with open("index.html", "r") as f:
                result = [(f.read() % (qs_d.get('a'),)).encode("UTF-8")]

    return result


serv = make_server("", 8080, app)
serv.serve_forever()
