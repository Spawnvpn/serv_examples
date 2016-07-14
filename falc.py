from wsgiref.simple_server import make_server

import falcon


class Resource:
    def on_get(self, req, res):
        res.body = '{ "message": "test" }'
        res.status = falcon.HTTP_200
        # req.params

api = falcon.API()
resource = Resource()
api.add_route("/", resource)

serv = make_server("", 8080, api)
serv.serve_forever()