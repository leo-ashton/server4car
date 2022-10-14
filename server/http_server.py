import http.server
import socketserver
import os

port = 8000


def run_http_server():

    os.chdir("./resources")

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("HTTP server serving at port", port)
        httpd.serve_forever()
