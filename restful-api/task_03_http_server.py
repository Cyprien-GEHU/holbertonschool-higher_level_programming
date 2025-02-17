#!/usr/bin/python3
"""
the programme will develop a simple API
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler_API(BaseHTTPRequestHandler):
    """
    The class Handler_API
    """
    def do_GET(self):
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.headers("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('uft-8'))

        elif self.path == '/':
            self.send_response(200)
            self.headers("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/status':
            self.send_response(200)
            self.headers("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == '/info':
            information = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            self.send_response(200)
            self.headers = {"Content-type": "application/json"}
            self.end_headers()
            self.wfile.write(json.dumps(information).encode('uft-8'))

        else:
            self.send_response(404)
            self.headers("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=Handler_API):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()