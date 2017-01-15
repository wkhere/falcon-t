import falcon

class FooResponder(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Foo!!'
        #..content_type 

app = application = falcon.API()
app.add_route('/', FooResponder()) 
