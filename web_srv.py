#!/usr/bin/env python3
import time
from redis import Redis
import sys

cli = Redis('localhost')

try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
except ImportError:
    sys.exit('ERROR: It seems like you are not running Python 3. '
             'This script only works with Python 3!')

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        temperature = float(cli.get('shared_temp').decode())
        alert= ""
        if (temperature > 22):
            alert="""<div class="alert alert-danger" role="alert">Temperature too high!</div>"""
        if (temperature < 20):
            alert="""<div class="alert alert-primary" role="alert">Temperature too low!</div>"""

        body = """
        <!doctype html>
        <html><head>
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        </head><body>
        <div class="container">
        """ + alert + """
        <h1>IoT temperature monitoring</h1>
        Temperature: """ + str(temperature) +  """&deg;C
        </div>
        <script>
        window.setTimeout(function(){
          window.location.reload(true)
        }, 2000);
        </script>
        </body></html>
        """
        self.wfile.write(bytes(body, 'UTF-8'))


if __name__ == '__main__':
    server = HTTPServer(('', 8081), MyHandler)
    print ("Starting web server on http://localhost:8081/")
    server.serve_forever()


