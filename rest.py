from bottle import (
    route,
    run,
    request,
    response
)
from core import (
    App
)

class Api:
    app = None

    def __init__(self, db):
        self.app = App(db)
        self.routes()
        run(host='0.0.0.0', port=6001)

    def resolve(self, callback):
        params = request.json
        resp   = callback(params)
        response.status = resp[1]
        return resp[0]

    def routes(self):
        
        @route('/', methods=['GET'])
        def home():
            response.set_header('Acess-Control-Allow-Origin', '*')
            response.status = 200
            return 'Hello Word.!'

        @route('/register', method=['POST', 'OPTIONS'])
        def register():
            return self.resolve( self.app.create )
