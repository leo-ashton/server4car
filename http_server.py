import http.server
import socketserver
import os

port = 8000


def run_http_server():

    os.chdir("car_server/resources")

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)
        httpd.serve_forever()
