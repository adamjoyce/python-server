
# code reduced from https://wiki.python.org/moin/BaseHttpServer

import time
import BaseHTTPServer

# example of a python class
 
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(s):
    """Respond to a GET request."""
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()

    slash = s.path.split('/', 1)
    num = slash[1].split('+', 1)
    result = int(num[0]) + int(num[1])

    s.wfile.write("<html><head><title>Title goes here.</title></head>")
    s.wfile.write("<body><p>This is a test.</p>")
    s.wfile.write("<p>Result: %s</p>" % result)
    s.wfile.write("</body></html>")


httpd = BaseHTTPServer.HTTPServer(("localhost", 8000), MyHandler)
httpd.serve_forever()

