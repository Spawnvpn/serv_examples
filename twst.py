from twisted.web import server, resource
from twisted.internet import reactor


class Simple(resource.Resource):
    isLeaf = True

    def render_GET(self, request):
        return "Hello"


site = server.Site(Simple())
reactor.listenTCP(19000, site)
reactor.run()
